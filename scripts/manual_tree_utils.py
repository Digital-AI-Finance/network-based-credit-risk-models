#manual_tree_utils.py

import itertools
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt

__all__ = [
    "grid_surrogate_trees",
    "select_pareto_models",
    "extract_rules",
    "fit_ova_trees",
    "plot_manual_partial_dependence",
    "plot_best_tree"
]

def grid_surrogate_trees(X, y, param_grid):
    """
    Fit DecisionTreeClassifier over a grid of hyperparameters.
    Returns dict name -> {'model', 'accuracy', 'n_leaves'}.
    """
    candidates = {}
    for max_depth in param_grid.get('max_depth', [None]):
        for min_samples_leaf in param_grid.get('min_samples_leaf', [1]):
            for max_features in param_grid.get('max_features', [None]):
                name = f"depth{max_depth}_leaf{min_samples_leaf}_feat{max_features}"
                model = DecisionTreeClassifier(
                    max_depth=max_depth,
                    min_samples_leaf=min_samples_leaf,
                    max_features=max_features,
                    random_state=0
                )
                model.fit(X, y)
                acc = accuracy_score(y, model.predict(X))
                n_leaves = model.get_n_leaves()
                candidates[name] = {
                    'model': model,
                    'accuracy': acc,
                    'n_leaves': n_leaves
                }
    return candidates

def select_pareto_models(candidates, performance_threshold=0.02):
    """
    Select models within performance_threshold of best accuracy.
    Returns dict name -> model.
    """
    best_acc = max(rec['accuracy'] for rec in candidates.values())
    selected = {}
    for name, rec in candidates.items():
        if rec['accuracy'] >= best_acc * (1 - performance_threshold):
            selected[name] = rec['model']
    return selected

def extract_rules(model, feature_names):
    """
    Extract human-readable rules from a DecisionTreeClassifier.
    Returns list of rule strings.
    """
    text = export_text(model, feature_names=list(feature_names))
    return text.split("\n")

def fit_ova_trees(X, y, max_depth=3, min_samples_leaf=10, max_features=None):
    """
    Fit a binary tree for each class (One-vs-All).
    Returns dict 'Regime {c}' -> model.
    """
    ova_models = {}
    unique_classes = sorted(set(y))
    for c in unique_classes:
        y_bin = (y == c).astype(int)
        name = f"Regime {c}"
        model = DecisionTreeClassifier(
            max_depth=max_depth,
            min_samples_leaf=min_samples_leaf,
            max_features=max_features,
            random_state=0
        )
        model.fit(X, y_bin)
        ova_models[name] = model
    return ova_models

def plot_manual_partial_dependence(models, X, features, grid_resolution=50):
    """
    Manual Partial Dependence: plot mean predicted probability as each feature
    varies over its observed range for One-vs-All models.
    """
    for name, model in models.items():
        fig, axes = plt.subplots(1, len(features), figsize=(4*len(features), 4))
        if len(features) == 1:
            axes = [axes]
        classes = model.classes_
        for ax, feat in zip(axes, features):
            vals = np.linspace(X[feat].min(), X[feat].max(), grid_resolution)
            mean_probs = []
            X_temp = X.copy()
            for v in vals:
                X_temp[feat] = v
                probs = model.predict_proba(X_temp)
                # for binary One-vs-All, take probability of class '1'
                if len(classes) == 2:
                    p = probs[:, list(classes).index(1)]
                else:
                    p = probs[:, 1]
                mean_probs.append(p.mean())
            ax.plot(vals, mean_probs)
            ax.set_title(f"{name}: {feat}")
            ax.set_xlabel(feat)
            ax.set_ylabel("Avg Prob")
        plt.tight_layout()
        plt.show()

def plot_best_tree(selected_models, candidates, X, feature_names=None,
                   class_prefix="Regime", figsize=(12,6), fontsize=10):
    """
    Selects the best model by accuracy and plots its decision tree.
    Returns the name of the best model and the model instance.
    """
    best_name = max(
        selected_models.keys(),
        key=lambda name: candidates[name]['accuracy']
    )
    best_model = selected_models[best_name]
    
    if feature_names is None:
        feature_names = list(X.columns)
    
    fig, ax = plt.subplots(1, 1, figsize=figsize)
    plot_tree(
        best_model,
        feature_names=feature_names,
        class_names=[f"{class_prefix} {c}" for c in best_model.classes_],
        filled=True,
        rounded=True,
        fontsize=fontsize,
        ax=ax
    )
    ax.set_title(f"Decision Tree: {best_name}")
    plt.tight_layout()
    plt.show()
    return best_name, best_model

