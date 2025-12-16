import os
import copy
import numpy as np
import pandas as pd

import cvxpy as cp
from hmmlearn import hmm

from scipy.stats import multivariate_normal
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

import sys
python_path = os.path.abspath(os.path.join(__file__ ,"../.."))
sys.path.append(python_path)
from utils import use_default

from models.clustering.r2kmeans import R2KMeans
from models.HMMs.base_hmm import BaseHMM

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

class R2GaussianHMM(BaseHMM):
    def __init__(self, n_components: int=None, covariance_type: str=None, n_iter: int=None, tol: float=None):
        super().__init__(n_components=n_components)
        self.covariance_type = use_default(covariance_type, "diag")
        self.n_iter = use_default(n_iter, 100)
        self.tol = use_default(tol, 1e-6)

        self.prev_regimes = None
        self.start_prob = None

        self.cluster_model = None
        #self.cluster_dump = None


    def process_data_input(self, data):  # ensure data is a dataframe

        # the algorithm requires a 3d numpy array, if not provided, it will try to trasnform it into one

        if isinstance(data, np.ndarray):
            return data
        elif isinstance(data, pd.DataFrame):
            # method for dataframe as input
            data = data.dropna(how='all')
            return data.values
        else:
            raise TypeError(f'ERROR -> data is not a numpy array, instead is {type(data)}')

    def fit(self, X):
        X_ = copy.deepcopy(X)

        X_ = self.process_data_input(X_)

        self.scaler = StandardScaler()
        self.scaler.fit(X_)
        X_ = self.scaler.transform(X_)

        if self.n_components is None:
            self.optimal_number_of_state(X_)

        if self.cluster_model is None:
            self.cluster_model = R2KMeans(self.n_components, init_method="k++", stable_init=True)
            self.start_prob = np.array([1.0] * self.n_components) / self.n_components
            self.prev_transmat_ = np.ones((self.n_components, self.n_components)) / self.n_components
        else:
            self.prev_transmat_ = None

        self.cluster_model.fit(X_)
        init_means = self.cluster_model.means

        self.model = hmm.GaussianHMM(n_components=self.n_components, covariance_type=self.covariance_type,
                                     n_iter=self.n_iter, tol=self.tol, init_params='')
        self.model.startprob_ = self.start_prob
        self.model.means_ = init_means
        if self.prev_transmat_ is not None:
            self.model.transmat_ = self.prev_transmat_
        self.model.fit(X_)

        regimes = self.get_model_regimes()

        if self.prev_regimes is not None:
            assign_mat, regimes = self.assign_labels(previous_regimes=self.prev_regimes, new_regimes=regimes)
            map_ = {old_idx: None for old_idx in range(assign_mat.shape[1])}
            new_added_count = 0
            num_old_regimes = assign_mat.shape[0]

            for old_idx in range(len(map_)):
                if assign_mat[:, old_idx].sum() == 0:
                    map_[old_idx] = num_old_regimes + new_added_count
                    new_added_count += 1
                else:
                    map_[old_idx] = np.where(assign_mat[:, old_idx] >= 0.9)[0][0]
            self.current_regime_index_remap = copy.deepcopy(map_)
            sorted_idx = np.arange(self.model.means_.shape[0])
            self.current_regime_index_remap = {old_idx: new_idx for new_idx, old_idx in enumerate(sorted_idx)}
        else:
            sorted_idx = np.argsort(self.model.means_[:, 0])
            self.current_regime_index_remap = {old_idx: new_idx for new_idx, old_idx in enumerate(sorted_idx)}

        sorted_idx = np.arange(self.model.means_.shape[0])
        self.current_regime_index_remap = {old_idx: new_idx for new_idx, old_idx in enumerate(sorted_idx)}
        self.prev_regimes = copy.deepcopy(regimes)


    def optimal_number_of_state(self, X_):
        is_score_decreasing = False
        self.n_components = 2
        best_silhouette_score = -1

        while True ^ is_score_decreasing:
            cluster_model = R2KMeans(self.n_components, init_method="k++", stable_init=True)
            cluster_model.fit(X_)
            init_means = cluster_model.means

            start_prob = np.array([1.0] * self.n_components) / self.n_components
            prev_transmat = np.ones((self.n_components, self.n_components)) / self.n_components
            model = hmm.GaussianHMM(
                n_components=self.n_components, covariance_type=self.covariance_type,
                n_iter=self.n_iter, tol=self.tol, init_params=''
            )
            model.startprob_ = start_prob
            model.transmat_ = prev_transmat
            model.means_ = init_means
            model.fit(X_)

            s_score = silhouette_score(X_, model.predict(X_))
            if s_score >= best_silhouette_score:
                self.n_components += 1
                best_silhouette_score = s_score
            else:
                is_score_decreasing = True
        self.n_components -= 1

    def current_transition(self):
        sorted_idx = list(self.current_regime_index_remap.keys())
        regime_list = ['{}'.format(i + 1) for i in range(len(self.current_regime_index_remap))]
        cur_trans = pd.DataFrame(self.model.transmat_[sorted_idx, :][:, sorted_idx], index=regime_list, columns=regime_list)
        return cur_trans

    def get_model_regimes(self):
        rv_list = [multivariate_normal(mean=self.model.means_[idx, :], cov=self.model.covars_[idx, ::]) for idx in range(self.model.means_.shape[0])]
        regime_dict = {f'{idx+1}': rv for idx, rv in enumerate(rv_list)}
        return regime_dict

    def pair_assignment_cost(self, rv1, rv2, alpha=0.7) -> float:
        """
        :param alpha: weights of mean cost
        """
        assert (alpha <= 1) and (alpha >= 0)
        mean_cost = np.linalg.norm(rv1.mean - rv2.mean, ord=2)
        cov_cost = np.linalg.norm(rv1.cov - rv2.cov, ord='fro')

        return alpha * mean_cost + (1 - alpha) * cov_cost

    def get_cost_matrix(self, past_regimes: dict, new_regimes: dict) -> np.ndarray:
        cost_mat = 10000 * np.ones(shape=(len(past_regimes), len(new_regimes)))

        for i, past_rv in enumerate(past_regimes.values()):
            for j, new_rv in enumerate(new_regimes.values()):
                cost_mat[i, j] = self.pair_assignment_cost(past_rv, new_rv)

        return cost_mat

    def assign_labels(self, previous_regimes: dict, new_regimes: dict) -> tuple:
        # calculate cost matrix
        cost_mat = self.get_cost_matrix(previous_regimes, new_regimes)
        num_old_regimes = cost_mat.shape[0]

        # decision variables
        x = cp.Variable((len(previous_regimes), len(new_regimes)), integer=True)

        # objective
        obj_func = cp.Minimize(cp.atoms.norm(cp.multiply(cost_mat, x), 'fro') / num_old_regimes)

        # model
        model = cp.Problem(
            objective=obj_func,
            constraints=[
                cp.sum(x, axis=0) <= 1,  # at most one label is assigned to a new regime
                cp.sum(x, axis=1) == 1,  # each label of the old regimes is assigned to exactly one new regime
                x >= 0  # indicator
            ]
        )

        # solve model
        obj = model.solve(solver='SCIP')
        # get assignment matrix
        assign_mat = x.value

        # relabel new_regimes based on assignment matrix

        previous_regime_labels = list(previous_regimes.keys())

        new_regime_labels = [None for _ in range(len(new_regimes))]
        newly_added_regime_labels = [f'{idx}' for idx in range(len(previous_regimes) + 1, len(new_regimes) + 1)]

        newly_added_count = 0
        for idx in range(len(new_regimes)):
            if np.where(assign_mat[:, idx] >= 0.9)[0].shape[0] == 0:
                new_regime_labels[idx] = newly_added_regime_labels[newly_added_count]
                newly_added_count += 1
            else:
                new_regime_labels[idx] = previous_regime_labels[np.where(assign_mat[:, idx] >= 0.9)[0][0]]

        return x.value, {new_label: regime for new_label, regime in zip(new_regime_labels, new_regimes.values())}


    def dump(self):
        reqs = self.base_dump()
        reqs["cluster_dump"] = self.cluster_model.dump()
        reqs["prev_regimes"] = self.prev_regimes
        reqs["current_regime_index_remap"] = self.current_regime_index_remap
        reqs["model"] = self.model
        reqs["start_prob"] = self.start_prob
        reqs["prev_transmat_"] = self.prev_transmat_

        return reqs

    def load(self, reqs):
        self.cluster_model = R2KMeans()
        self.cluster_model.load(reqs["cluster_dump"])
        self.base_load(reqs)
        self.prev_regimes = reqs["prev_regimes"]
        self.current_regime_index_remap = reqs["current_regime_index_remap"]
        self.model = reqs["model"]
        self.start_prob = reqs["start_prob"]
        self.prev_transmat_ = reqs["prev_transmat_"]
