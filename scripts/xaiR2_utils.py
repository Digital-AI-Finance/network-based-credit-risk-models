#xaiR2_1

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from IPython.display import display
from scipy import stats
from models.embedding.R2PCA import R2PCA_I
from models.HMMs.r2_gaussian_hmm import R2GaussianHMM
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier, plot_tree
from lightgbm import LGBMClassifier
import shap
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.metrics import accuracy_score
from collections import deque

__all__ = [
    # Step 3.1–3.2
    "compute_state_stats",
    "display_state_stats",
    "plot_state_heatmaps",
    "profile_indicators_by_regime",
    # Step 3.3
    "compute_pc_deep_dive",
    "plot_pc_deep_dive",
    # Step 3.4
    "compute_sensitivity_dfs",
    "plot_sensitivity_dfs",
    # Step 3.4 robust
    "validate_hmm",
    # Step 3.5
    "plot_transition_matrix",
    "plot_indicators_shaded",
    # Step 3.6
    "fit_l1_logistic",
    "plot_l1_coeffs",
    "fit_surrogate_tree",
    "plot_surrogate_tree_model",
    "fit_single_stump",
    "equential_stumps",
    # Step 3.7
    "run_tree_shap",
    "plot_shap_global_importance",
    "plot_shap_class_conditional",
    "plot_shap_summary",
    "rolling_explainers"
]

def compute_state_stats(final_regime_model, selected_indicators):
    """
    Extract state-specific means and variances from the fitted HMM model.
    Returns (means_df, vars_df).
    """
    # 1) Pull out the learned Gaussian means and covariances
    means_array = final_regime_model.model.means_            # shape: (n_states, n_features)
    covars = final_regime_model.model.covars_                # diag or full

    # 2) Build DataFrames
    n_states = means_array.shape[0]
    state_labels = [f"Regime {i+1}" for i in range(n_states)]
    means_df = pd.DataFrame(
        means_array,
        index=state_labels,
        columns=selected_indicators
    )
    if covars.ndim == 2:
        vars_df = pd.DataFrame(
            covars,
            index=state_labels,
            columns=selected_indicators
        )
    else:
        diag_vars = [np.diag(covars[i]) for i in range(n_states)]
        vars_df = pd.DataFrame(
            diag_vars,
            index=state_labels,
            columns=selected_indicators
        )
    return means_df, vars_df

def display_state_stats(means_df, vars_df):
    """
    Print and display state-specific means and variances.
    """
    print("▶︎ State‑specific Means:")
    display(means_df)
    print("\n▶︎ State‑specific Variances:")
    display(vars_df)

def plot_state_heatmaps(means_df, vars_df, figsize=(8, 4), cmap_means="vlag", cmap_vars="vlag", center_means=0):
    """
    Plot heatmaps of state-specific means and variances.
    """
    plt.figure(figsize=figsize)
    sns.heatmap(means_df, annot=True, fmt=".2f", cmap=cmap_means, center=center_means)
    plt.title("Regime Means by Indicator")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=figsize)
    sns.heatmap(vars_df, annot=True, fmt=".2f", cmap=cmap_vars)
    plt.title("Regime Variances by Indicator")
    plt.tight_layout()
    plt.show()

def profile_indicators_by_regime(df_reduced_imputed, df_probs, selected_indicators):
    """
    Visual profiling of indicators by regime:
      - Boxplots of indicator distributions by regime
      - Regime-conditioned correlation matrices
      - Print regime share percentages
    """
    # Copy posterior+label DataFrame
    final_regime_probs = df_probs.copy()

    # Align to available dates
    aligned = df_reduced_imputed.loc[final_regime_probs.index]

    # Prepare for melt
    vis_df2 = aligned.reset_index()
    old_index_col = vis_df2.columns[0]
    vis_df2 = vis_df2.rename(columns={old_index_col: 'Date'})
    vis_df2['Regime'] = final_regime_probs['RegimeLabel'].astype(int).values

    # Melt for boxplots
    melted = vis_df2.melt(
        id_vars=['Date', 'Regime'],
        value_vars=selected_indicators,
        var_name='Indicator',
        value_name='Value'
    )

    # Boxplots per indicator
    g = sns.FacetGrid(melted, col='Indicator', col_wrap=4, sharey=False, height=3.5)
    g.map_dataframe(sns.boxplot, x='Regime', y='Value', palette="Set2")
    g.set_titles("{col_name}")
    g.fig.suptitle("Indicator Distributions by Regime", y=1.02)
    plt.tight_layout()
    plt.show()

    # Regime-conditioned correlation matrices
    for r in sorted(vis_df2['Regime'].unique()):
        subset = vis_df2[vis_df2['Regime'] == r][selected_indicators]
        corr = subset.corr()
        plt.figure(figsize=(6, 5))
        sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', vmin=-1, vmax=1)
        plt.title(f'Correlation Matrix: Regime {r}')
        plt.tight_layout()
        plt.show()

    # Print regime share
    counts = (
        final_regime_probs['RegimeLabel']
        .value_counts(normalize=True)
        .sort_index()
        * 100
    )
    for reg_id, pct in counts.items():
        print(f"Regime {reg_id} share: {pct:.2f}%")

def compute_pc_deep_dive(df_scaled_regime, final_regime_probs, selected_indicators):
    """
    Recompute regime-conditioned PC1–PC3 loadings.
    Returns (loadings_3pc, pc_loadings).
    """
    regime_series = final_regime_probs['RegimeLabel'].astype(int)
    regimes = sorted(regime_series.unique())
    loadings_3pc = {}
    for r in regimes:
        idx_r = regime_series[regime_series == r].index
        df_r = df_scaled_regime.loc[idx_r, selected_indicators].dropna()
        if df_r.shape[0] <= 3:
            continue
        mdl = R2PCA_I(n_components=3, pct_variance=None, hierarchical=False)
        mdl.fit(df_r, curr_names=selected_indicators)
        loadings_3pc[r] = mdl.prev_eigenvectors_
    pc_loadings = {
        i+1: pd.DataFrame(
            {r: loadings_3pc[r][i] for r in loadings_3pc},
            index=selected_indicators
        ).T
        for i in range(3)
    }
    return loadings_3pc, pc_loadings


def plot_pc_deep_dive(pc_loadings, figsize=(12, 4), cmap="vlag", center=0):
    """
    Plot the heatmaps for PC1–PC3 loadings side by side.
    """
    fig = plt.figure(figsize=figsize, constrained_layout=True)
    gs = gridspec.GridSpec(1, 4, figure=fig, width_ratios=[1, 1, 1, 0.05])
    ax0 = fig.add_subplot(gs[0, 0])
    ax1 = fig.add_subplot(gs[0, 1], sharey=ax0)
    ax2 = fig.add_subplot(gs[0, 2], sharey=ax0)
    cax = fig.add_subplot(gs[0, 3])
    sns.heatmap(pc_loadings[1], annot=True, fmt=".2f", cmap=cmap, center=center, cbar=False, ax=ax0)
    ax0.set_title("PC1 Loadings"); ax0.set_xlabel("Indicator"); ax0.set_ylabel("Regime")
    sns.heatmap(pc_loadings[2], annot=True, fmt=".2f", cmap=cmap, center=center, cbar=False, ax=ax1)
    ax1.set_title("PC2 Loadings"); ax1.set_xlabel("Indicator")
    sns.heatmap(pc_loadings[3], annot=True, fmt=".2f", cmap=cmap, center=center, cbar=True, cbar_ax=cax, ax=ax2)
    ax2.set_title("PC3 Loadings"); ax2.set_xlabel("Indicator")
    plt.show()


def compute_sensitivity_dfs(loadings_3pc, df_scaled_regime, final_regime_probs, selected_indicators):
    """
    Compute eigen-perturbation sensitivity for PCs 1–3.
    Returns dicts sensitivity_by_pc and sensitivity_dfs.
    """
    regime_series = final_regime_probs['RegimeLabel'].astype(int)
    sensitivity_by_pc = {i+1: {} for i in range(3)}
    for r, loadings in loadings_3pc.items():
        idx_r = regime_series[regime_series == r].index
        df_r = df_scaled_regime.loc[idx_r, selected_indicators].dropna()
        sigma = df_r.std(axis=0).values
        for i in range(3):
            sensitivity_by_pc[i+1][r] = np.abs(loadings[i, :]) * sigma
    sensitivity_dfs = {
        i: pd.DataFrame(sensitivity_by_pc[i], index=selected_indicators).T
        for i in range(1, 4)
    }
    return sensitivity_by_pc, sensitivity_dfs


def plot_sensitivity_dfs(sensitivity_dfs, figsize=(14, 4), cmap="vlag", annot_kws={"fontsize":6}):
    """
    Plot heatmaps of eigen-perturbation sensitivity for PCs 1–3.
    """
    fig = plt.figure(figsize=figsize, constrained_layout=True)
    gs = gridspec.GridSpec(1, 4, figure=fig, width_ratios=[1, 1, 1, 0.05])
    ax0 = fig.add_subplot(gs[0, 0])
    ax1 = fig.add_subplot(gs[0, 1], sharey=ax0)
    ax2 = fig.add_subplot(gs[0, 2], sharey=ax0)
    cax = fig.add_subplot(gs[0, 3])
    sns.heatmap(sensitivity_dfs[1], annot=True, fmt=".2f", cmap=cmap, cbar=False, ax=ax0, annot_kws=annot_kws)
    ax0.set_title("Eigen-Perturbation PC1"); ax0.set_ylabel("Regime"); ax0.set_xlabel("Indicator")
    sns.heatmap(sensitivity_dfs[2], annot=True, fmt=".2f", cmap=cmap, cbar=False, ax=ax1, annot_kws=annot_kws)
    ax1.set_title("Eigen-Perturbation PC2"); ax1.set_xlabel("Indicator")
    sns.heatmap(sensitivity_dfs[3], annot=True, fmt=".2f", cmap=cmap, cbar=True, cbar_ax=cax, ax=ax2, annot_kws=annot_kws)
    ax2.set_title("Eigen-Perturbation PC3"); ax2.set_xlabel("Indicator")
    plt.show()


def validate_hmm(training_data, best_k, df_scaled_regime, df_probs, test_start='2011-01-01'):
    """
    Perform Vuong test, AIC/BIC, out-of-sample LL back-test,
    and plot smoothed probabilities & Viterbi path.
    Returns models (model1, modelk) and metrics dict.
    """
    # Fit models
    model1 = R2GaussianHMM(n_components=1, n_iter=1000, tol=1e-5)
    model1.fit(training_data)
    modelk = R2GaussianHMM(n_components=best_k, n_iter=1000, tol=1e-5)
    modelk.fit(training_data)
    # Vuong test
    lp1 = np.array([model1.model.score(x.reshape(1,-1)) for x in training_data])
    lp2 = np.array([modelk.model.score(x.reshape(1,-1)) for x in training_data])
    d_train = lp2 - lp1; N = d_train.shape[0]
    V_stat = np.sqrt(N) * d_train.mean() / d_train.std(ddof=1)
    p_val = 2 * (1 - stats.norm.cdf(abs(V_stat)))
    # AIC/BIC
    def num_params(k, d): return (k-1) + k*(k-1) + 2*k*d
    d = training_data.shape[1]
    p1 = num_params(1, d); pk = num_params(best_k, d)
    LL1 = model1.model.score(training_data); LLk = modelk.model.score(training_data)
    AIC1 = -2*LL1 + 2*p1; AICk = -2*LLk + 2*pk
    BIC1 = -2*LL1 + p1*np.log(N); BICk = -2*LLk + pk*np.log(N)
    print(f"\nVuong Test (per-sample): V = {V_stat:.3f}, p-value = {p_val:.3f}")
    print(f"\n{'Model':<12}{'LL':>10}{'p':>6}{'AIC':>10}{'BIC':>10}")
    # in-sample comparison
    label1 = "1-state"
    labelk = f"{best_k}-state"
    print(f"{label1:<12}{LL1:10.2f}{p1:6d}{AIC1:10.2f}{BIC1:10.2f}")
    print(f"{labelk:<12}{LLk:10.2f}{pk:6d}{AICk:10.2f}{BICk:10.2f}")
    # Out-of-sample
    test_df = df_scaled_regime.loc[test_start:]
    cum1 = [model1.model.score(test_df.values[:i]) for i in range(1, len(test_df)+1)]
    cumk = [modelk.model.score(test_df.values[:i]) for i in range(1, len(test_df)+1)]
    dates_test = test_df.index
    cum1 = np.array(cum1); cumk = np.array(cumk); delta = cumk - cum1
    # Plot
    plt.figure(figsize=(10,4));
    plt.plot(dates_test, cum1, label="1-State HMM"); plt.plot(dates_test, cumk, label=f"{best_k}-State HMM")
    plt.title("Out-of-Sample Cumulative Log-Likelihood"); plt.xlabel("Date"); plt.ylabel("Cumulative LL"); plt.legend(); plt.tight_layout(); plt.show()
    plt.figure(figsize=(10,3)); plt.plot(dates_test, delta, label='Δ LL (cum)'); plt.axhline(0, color='k', ls='--');
    mask = delta < 0
    plt.fill_between(dates_test, delta, 0, where=mask, color='red', alpha=0.2, label='1-state wins')
    plt.fill_between(dates_test, delta, 0, where=~mask, color='green', alpha=0.2, label=f'{best_k}-state wins')
    plt.title("Cumulative Δ Log-Likelihood (Out-of-Sample)"); plt.xlabel("Date"); plt.ylabel("Δ Log-Likelihood"); plt.legend(loc='upper left'); plt.tight_layout(); plt.show()
    # Smoothed probabilities
    prob_cols = [f"P{i+1}" for i in range(best_k)]
    smoothed = df_probs[prob_cols].astype(float).copy()
    smoothed.columns = [f"Regime {i+1}" for i in range(best_k)]
    plt.figure(figsize=(12,3)); ax = smoothed.plot.area(alpha=0.6)
    ax.legend(title="Regime", loc='upper left', bbox_to_anchor=(1.02,1), ncol=1, frameon=False)
    ax.set_title("Smoothed State Probabilities"); ax.set_ylabel("Probability"); ax.set_xlabel(""); plt.tight_layout(); plt.show()
    # Viterbi
    decoded = modelk.model.predict(df_scaled_regime.values) + 1
    plt.figure(figsize=(12,2)); plt.step(df_scaled_regime.index, decoded, where='post'); plt.yticks(range(1, best_k+1)); plt.title("Viterbi‑Decoded Regimes"); plt.xlabel("Date"); plt.tight_layout(); plt.show()
    metrics = {'V_stat': V_stat, 'p_val': p_val,
               'AIC1': AIC1, 'AICk': AICk, 'BIC1': BIC1, 'BICk': BICk,
               'delta': delta, 'dates_test': dates_test}
    return model1, modelk, metrics

def plot_transition_matrix(final_regime_model, figsize=(6,5), cmap="Blues"):
    """
    Plot HMM transition matrix heatmap.
    """
    trans = final_regime_model.model.transmat_
    labels = [f"Regime {i+1}" for i in range(trans.shape[0])]
    plt.figure(figsize=figsize)
    sns.heatmap(trans, annot=True, fmt=".2f", cmap=cmap,
                xticklabels=labels, yticklabels=labels,
                cbar_kws={"label": "P( next | current )"})
    plt.title("HMM Transition Matrix"); plt.xlabel("Next Regime"); plt.ylabel("Current Regime"); plt.tight_layout(); plt.show()


def plot_indicators_shaded(df_reduced_imputed, final_regime_probs, selected_indicators, figsize_scale=(5,3)):
    """
    Plot selected indicators over time with regime shading.
    """
    df_plot = df_reduced_imputed.loc[final_regime_probs.index]
    dates = df_plot.index
    regimes = final_regime_probs['RegimeLabel'].astype(int)
    unique_regs = sorted(regimes.unique())
    palette = plt.get_cmap("tab10")
    reg_color = {r: palette(i) for i, r in enumerate(unique_regs)}
    change = regimes.ne(regimes.shift())
    segment_starts = dates[change]
    segment_regs = regimes[change].values
    segment_ends = segment_starts[1:].tolist() + [dates[-1]]
    n = len(selected_indicators)
    cols = 3; rows = int(np.ceil(n/cols))
    fig, axes = plt.subplots(rows, cols, figsize=(cols*figsize_scale[0], rows*figsize_scale[1]), sharex=True)
    axes = axes.flatten()
    for ax, ind in zip(axes, selected_indicators):
        ax.plot(dates, df_plot[ind], color='black')
        for start, end, r in zip(segment_starts, segment_ends, segment_regs):
            ax.axvspan(start, end, color=reg_color[r], alpha=0.2)
        ax.set_title(ind); ax.grid(False)
    for ax in axes[n:]: ax.set_visible(False)
    handles = [plt.Rectangle((0,0),1,1, color=reg_color[r], alpha=0.2) for r in unique_regs]
    labels = [f"Regime {r}" for r in unique_regs]
    fig.legend(handles, labels, loc='upper right', title="Regimes")
    fig.suptitle("Selected Indicators Over Time with Regime Shading", y=1.02)
    fig.autofmt_xdate(); plt.tight_layout(); plt.show()

    # --- Step 3.6: Glass‑box via L1‑Logistic Regression & Surrogate Tree — Functions


def fit_l1_logistic(
    df_regime_std: pd.DataFrame,
    final_regime_probs: pd.DataFrame,
    selected_indicators: list[str],
    C: float = 1.0,
    random_state: int = 0
) -> tuple[LogisticRegression, pd.DataFrame, pd.Series, float, pd.DataFrame]:
    """
    Fit an L1‑regularized multiclass logistic regression including regime duration.
    Returns (clf_lr, X, y, accuracy, coef_df).
    """
    # compute "time in current regime"
    regime_series = final_regime_probs['RegimeLabel'].astype(int)
    durations = (
        regime_series
        .ne(regime_series.shift())
        .cumsum()
        .groupby(regime_series)
        .cumcount() + 1
    )
    final_regime_probs['RegimeDuration'] = durations.values

    # prepare features and target
    X = df_regime_std[selected_indicators].loc[final_regime_probs.index].copy()
    X['Duration'] = final_regime_probs['RegimeDuration']
    y = final_regime_probs['RegimeLabel'].astype(int)

    # fit logistic regression
    clf_lr = LogisticRegression(
        penalty='l1', C=C,
        solver='saga', multi_class='multinomial',
        max_iter=1000, random_state=random_state
    )
    clf_lr.fit(X, y)

    # compute in‑sample accuracy
    acc = accuracy_score(y, clf_lr.predict(X))

    # build coefficient DataFrame
    coefs = clf_lr.coef_
    classes = clf_lr.classes_
    if coefs.shape[0] == 1 and len(classes) == 2:
        coefs = np.vstack([-coefs, coefs])
        idx = [f"Regime {c}" for c in classes]
    else:
        idx = [f"Regime {c}" for c in classes]
    coef_df = pd.DataFrame(coefs, index=idx, columns=X.columns)

    return clf_lr, X, y, acc, coef_df


def plot_l1_coeffs(
    coef_df: pd.DataFrame,
    figsize: tuple[int,int] = (10, None)
) -> None:
    """
    Plot heatmap of L1‑logistic coefficients by regime.
    """
    n_regs = coef_df.shape[0]
    height = max(4, n_regs * 0.8)
    fig, ax = plt.subplots(figsize=(figsize[0], height))
    sns.heatmap(
        coef_df,
        annot=True,
        fmt=".2f",
        cmap="vlag",
        center=0,
        linewidths=0.5,
        linecolor="white",
        cbar_kws={"label": "Coefficient"},
        ax=ax
    )
    ax.set_yticklabels(
        ax.get_yticklabels(),
        rotation=0,
        va="center",
        fontsize=10
    )
    plt.subplots_adjust(left=0.25, right=0.95, top=0.90, bottom=0.10)
    ax.set_title("L₁‑Logistic Coeffs by Regime (with Duration)")
    ax.set_ylabel("Regime")
    plt.tight_layout()
    plt.show()


def fit_surrogate_tree(
    df_regime_std: pd.DataFrame,
    final_regime_probs: pd.DataFrame,
    selected_indicators: list[str],
    max_depth_options: list[int] = [2,3,4],
    min_samples_leaf_options: list[int] = [5,10,20],
    cv_folds: int = 5,
    random_state: int = 0
) -> tuple[DecisionTreeClassifier, pd.DataFrame, pd.Series, list[str], float]:
    """
    Cross‑validated surrogate decision tree:
     1) Grid‑search over max_depth and min_samples_leaf via StratifiedKFold CV
     2) Re‑fit on full data using best params
     3) Return (surrogate, X_tree, y_tree, top_feats, mean_cv_accuracy)
    """
    # Prepare data
    X_tree = df_regime_std[selected_indicators].loc[final_regime_probs.index]
    y_tree = final_regime_probs['RegimeLabel'].astype(int)

    # Hyperparameter CV
    kf = StratifiedKFold(n_splits=cv_folds, shuffle=True, random_state=random_state)
    best_score = -1.0
    best_params = {}
    for md in max_depth_options:
        for ms in min_samples_leaf_options:
            clf = DecisionTreeClassifier(
                max_depth=md,
                min_samples_leaf=ms,
                class_weight='balanced',
                random_state=random_state
            )
            scores = cross_val_score(clf, X_tree, y_tree, cv=kf, scoring='accuracy')
            if scores.mean() > best_score:
                best_score = scores.mean()
                best_params = {'max_depth': md, 'min_samples_leaf': ms}

    # Final fit on full data
    surrogate = DecisionTreeClassifier(
        **best_params,
        class_weight='balanced',
        random_state=random_state
    )
    surrogate.fit(X_tree, y_tree)

    # Extract top‑5 features by importance
    importances = pd.Series(
        surrogate.feature_importances_,
        index=X_tree.columns
    ).sort_values(ascending=False)
    top_feats = importances.head(5).index.tolist()

    return surrogate, X_tree, y_tree, top_feats, best_score


def plot_surrogate_tree_model(
    surrogate: DecisionTreeClassifier,
    feature_names: list[str],
    class_names: list[str],
    figsize: tuple[int,int] = (12,6),
    fontsize: int = 8
) -> None:
    """
    Visualize the surrogate decision tree.
    """
    plt.figure(figsize=figsize)
    plot_tree(
        surrogate,
        feature_names=feature_names,
        class_names=class_names,
        filled=True,
        rounded=True,
        fontsize=fontsize
    )
    plt.title("Surrogate Decision Tree", pad=20)
    plt.tight_layout()
    plt.show()


# --- Step 3.7: GBDT + TreeSHAP for Regime Classification Explainability — Functions

def run_tree_shap(
    df_regime_std: pd.DataFrame,
    final_regime_probs: pd.DataFrame,
    top_feats: list[str],
    train_frac: float = 0.8,
    n_estimators: int = 200,
    learning_rate: float = 0.05,
    random_state: int = 0
) -> tuple[
    LGBMClassifier, object, list[np.ndarray],
    pd.DataFrame, pd.DataFrame, pd.Series, pd.Series, list[str],
    pd.DataFrame, pd.DataFrame
]:
    """
    Fit LightGBM on top_feats and compute SHAP values.
    Returns (clf, explainer, shap_values_list,
             X_train, X_test, y_train, y_test,
             class_labels, imp_df, df_class_imp).
    """
    X_tree = df_regime_std[top_feats].loc[final_regime_probs.index]
    y_tree = final_regime_probs['RegimeLabel'].astype(int)

    split = int(len(X_tree) * train_frac)
    X_train, X_test = X_tree.iloc[:split], X_tree.iloc[split:]
    y_train, y_test = y_tree.iloc[:split], y_tree.iloc[split:]

    clf = LGBMClassifier(
        n_estimators=n_estimators,
        learning_rate=learning_rate,
        random_state=random_state
    )
    clf.fit(X_train, y_train)

    explainer = shap.TreeExplainer(clf)
    sv = explainer.shap_values(X_test)

    if isinstance(sv, list):
        shap_values_list = sv
    elif isinstance(sv, np.ndarray) and sv.ndim == 3:
        shap_values_list = [sv[:, :, i] for i in range(sv.shape[2])]
    elif isinstance(sv, np.ndarray) and sv.ndim == 2 and len(clf.classes_) == 2:
        pos = sv; neg = -pos
        shap_values_list = [neg, pos]
    else:
        raise ValueError(f"Unexpected shap_values shape {sv.shape}")

    class_labels = [f"Regime {c}" for c in clf.classes_]

    abs_shaps = [np.abs(arr) for arr in shap_values_list]
    stacked = np.stack(abs_shaps, axis=2)
    mean_abs = np.mean(stacked, axis=(0,2))
    imp_df = pd.DataFrame({"Feature": X_test.columns, "Mean|SHAP|": mean_abs})
    imp_df.sort_values("Mean|SHAP|", ascending=False, inplace=True)

    mean_per_class = np.stack(
        [np.abs(shap_values_list[i]).mean(axis=0) for i in range(len(class_labels))],
        axis=1
    )
    df_class_imp = pd.DataFrame(
        mean_per_class,
        index=X_test.columns,
        columns=class_labels
    )

    return (
        clf, explainer, shap_values_list,
        X_train, X_test, y_train, y_test,
        class_labels, imp_df, df_class_imp
    )


def plot_shap_global_importance(
    imp_df: pd.DataFrame,
    top_feats: list[str],
    figsize: tuple[int,int] = (6,4)
) -> None:
    """
    Plot global mean |SHAP| importance for top_feats.
    """
    n = len(top_feats)
    fig, ax = plt.subplots(figsize=figsize)
    ax.barh(
        imp_df['Feature'].iloc[:n][::-1],
        imp_df['Mean|SHAP|'].iloc[:n][::-1]
    )
    ax.set_xlabel("Mean |SHAP value|")
    ax.set_title("GBDT Global Importance on Tree‑Selected Features")
    plt.tight_layout()
    plt.show()


def plot_shap_class_conditional(
    df_class_imp: pd.DataFrame,
    figsize: tuple[int,int] = (10,6)
) -> None:
    """
    Plot class-conditional feature importance heatmap.
    """
    plt.figure(figsize=figsize)
    sns.heatmap(
        df_class_imp, annot=True, fmt=".2f",
        cmap="YlGnBu"
    )
    plt.title("Class-Conditional Feature Importance")
    plt.xlabel("Regime")
    plt.ylabel("Indicator")
    plt.tight_layout()
    plt.show()


def plot_shap_summary(
    shap_values_list: list[np.ndarray],
    X_test: pd.DataFrame,
    class_labels: list[str]
) -> None:
    """
    Plot SHAP summary plots for each regime.
    """
    for i, lab in enumerate(class_labels):
        shap.summary_plot(
            shap_values_list[i],
            X_test,
            feature_names=X_test.columns,
            show=False
        )
        plt.title(f"SHAP Summary for {lab}", pad=15, fontsize=14)
        plt.tight_layout()
        plt.show()

def fit_single_stump(
    X, y,
    min_samples_leaf: int,
    cv_folds: int,
    random_state: int
):
    """
    Fit a depth‐1 decision stump on (X,y) and return (stump, mean_cv_accuracy).
    """
    clf = DecisionTreeClassifier(
        max_depth=1,
        min_samples_leaf=min_samples_leaf,
        class_weight='balanced',
        random_state=random_state
    )
    cv = StratifiedKFold(n_splits=cv_folds, shuffle=True, random_state=random_state)
    scores = cross_val_score(clf, X, y, cv=cv, scoring='accuracy')
    clf.fit(X, y)
    return clf, scores.mean()

def sequential_stumps(
    X: pd.DataFrame,
    y: pd.Series,
    features: list[str],
    max_depth: int = 4,
    min_samples_leaf: int = 20,
    cv_folds: int = 5,
    min_gain: float = 0.0,
    baseline_accuracy: float = 0.5,
    random_state: int = 0
) -> dict[str, tuple[DecisionTreeClassifier,float,int]]:
    """
    Build a hierarchy of decision‐stumps (single splits) up to `max_depth`.
    Returns a dict mapping `node_path` → (stump, cv_accuracy, n_samples).
    
    node_path is a string of 'L'/'R' letters indicating the sequence of 
    left/right splits from the root ('' = root, 'L' = left child of root, etc.).
    
    Splits are only accepted if they (a) have ≥ min_samples_leaf in each child 
    and (b) improve CV accuracy over the parent by at least min_gain.
    """
    results = {}
    # queue entries: (node_path, X_sub, y_sub, parent_acc, depth)
    queue = deque([('', X, y, baseline_accuracy, 0)])
    
    while queue:
        path, X_sub, y_sub, parent_acc, depth = queue.popleft()
        # stop if we’ve reached max depth or too few samples
        if depth >= max_depth or len(y_sub) < 2 * min_samples_leaf:
            continue
        
        # fit & evaluate stump on this node
        stump, cv_acc = fit_single_stump(
            X_sub[features],
            y_sub,
            min_samples_leaf=min_samples_leaf,
            cv_folds=cv_folds,
            random_state=random_state
        )
        
        # require a gain
        if cv_acc - parent_acc < min_gain:
            continue
        
        # record it
        results[path] = (stump, cv_acc, len(y_sub))
        
        # identify split rule
        tree = stump.tree_
        feat_idx = tree.feature[0]
        thresh    = tree.threshold[0]
        feat_name = features[feat_idx]
        
        # partition the data
        left_mask  = X_sub[feat_name] <= thresh
        right_mask = ~left_mask
        
        X_left,  y_left  = X_sub[left_mask],  y_sub[left_mask]
        X_right, y_right = X_sub[right_mask], y_sub[right_mask]
        
        # enqueue children
        queue.append((path + 'L', X_left,  y_left,  cv_acc, depth + 1))
        queue.append((path + 'R', X_right, y_right, cv_acc, depth + 1))
    
    return results

def rolling_explainers(
    df_regime_std: pd.DataFrame,
    final_regime_probs: pd.DataFrame,
    selected_indicators: list[str],
    window_months: int = 6,
    step_months: int   = 1,
    *,
    sur_kwargs: dict | None = None,
    **stump_kwargs
) -> dict[pd.Timestamp, dict]:
    """
    Runs both fit_surrogate_tree and sequential_stumps
    on rolling windows of length `window_months` stepping by `step_months`.
    Automatically caps cv_folds at the minimum class count in each window
    and skips any window that still cannot satisfy fold constraints.
    - sur_kwargs: passed to fit_surrogate_tree (may include its cv_folds)
    - stump_kwargs: passed to sequential_stumps (may include its cv_folds)
    Returns a dict end_date -> {
        'surrogate_feats': list[str],
        'surrogate_acc': float,
        'stumps': dict[node_path, tuple(model, cv_acc, n_samples)]
    }.
    """
    # Local imports
    from pandas import date_range, DateOffset

    if sur_kwargs is None:
        sur_kwargs = {}

    ends = date_range(
        start=df_regime_std.index[window_months - 1],
        end=df_regime_std.index[-1],
        freq=f'{step_months}M'
    )
    results: dict[pd.Timestamp, dict] = {}

    for end in ends:
        # Define window
        start = end - DateOffset(months=window_months)
        mask  = (df_regime_std.index > start) & (df_regime_std.index <= end)
        Xw = df_regime_std.loc[mask]
        yw = final_regime_probs.loc[mask, 'RegimeLabel']

        # Skip if too few observations for splitting
        min_leaf = stump_kwargs.get('min_samples_leaf', 10)
        if len(yw) < 2 * min_leaf:
            continue

        # Compute safe cv_folds based on smallest class count
        class_counts = yw.value_counts()
        if class_counts.empty or class_counts.min() < 2:
            # Not enough cases for even 2 folds
            continue
        safe_cv = min(stump_kwargs.get('cv_folds', 5), class_counts.min())

        # Override cv_folds in both surrogate and stump settings
        sur_kwargs_window   = {**sur_kwargs,   'cv_folds': safe_cv}
        stump_kwargs_window = {**stump_kwargs, 'cv_folds': safe_cv}

        # 1) Fit surrogate tree and 2) hierarchical stumps with error guard
        try:
            sur, *_ , feats, acc = fit_surrogate_tree(
                Xw,
                final_regime_probs.loc[mask],
                selected_indicators,
                **sur_kwargs_window
            )
            stumps = sequential_stumps(
                Xw[selected_indicators],
                yw.astype(int),
                selected_indicators,
                **stump_kwargs_window
            )
        except ValueError:
            # Skip this window if CV constraints fail internally
            continue

        # Store results
        results[end] = {
            'surrogate_feats': feats,
            'surrogate_acc':   acc,
            'stumps':          stumps
        }

    return results