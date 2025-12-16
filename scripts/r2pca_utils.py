# r2pca_utils.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from models.embedding.R2PCA import R2PCA_I

__all__ = [
    "compute_full_pca",
    "determine_K",
    "plot_scree",
    "rolling_r2pca",
    "plot_rolling_scores",
    "select_top_indicators",
    "compute_loading_share",
    "get_indicator_metadata"
]

def compute_full_pca(
    df: pd.DataFrame,
    pct_variance: float = 0.75,
    hierarchical: bool = False
) -> tuple[np.ndarray, float]:
    """
    Fit a full‑sample R2‑PCA to df, return (ratios, total_variance).
    ratios[i] = explained‐variance by PC (i+1) as fraction of total.
    """
    pca = R2PCA_I(pct_variance=pct_variance, hierarchical=hierarchical)
    pca.fit(df, curr_names=list(df.columns))
    eigs = np.real(pca.val)
    total = pca.total_var
    ratios = eigs / total
    return ratios, total


def determine_K(
    ratios: np.ndarray,
    pct_threshold: float = 0.75,
    fixed_K: int | None = None
) -> int:
    """
    If fixed_K is given, returns that (but warns if cumvar < threshold).
    Otherwise picks the smallest k where ratios[:k].sum() >= pct_threshold.
    """
    if fixed_K is not None:
        cum = ratios[:fixed_K].sum()
        if cum < pct_threshold:
            print(f"⚠️ Warning: first {fixed_K} PCs explain only {cum:.2%}")
        else:
            print(f"✅ First {fixed_K} PCs explain {cum:.2%}")
        return fixed_K

    cum = 0.0
    for i, r in enumerate(ratios, start=1):
        cum += r
        if cum >= pct_threshold:
            print(f"→ Chose K={i} (cumulative {cum:.2%})")
            return i

    print("⚠️ Threshold not reached; defaulting to full set.")
    return len(ratios)


def plot_scree(
    ratios: np.ndarray,
    K: int,
    pct_threshold: float = 0.75,
    max_pc: int = 20,
    figsize=(6,4)
):
    """Plot cumulative explained‑variance up to max_pc, mark K and threshold."""
    cumratios = np.cumsum(ratios)
    plt.figure(figsize=figsize)
    xs = np.arange(1, len(ratios)+1)
    plt.plot(xs, cumratios, marker="o")
    plt.axvline(K, color="gray", ls="--", label=f"PC{K} cutoff")
    plt.axhline(pct_threshold, color="red", ls="--", label=f"{pct_threshold:.0%} target")
    plt.xlim(1, min(max_pc, len(ratios)))
    plt.ylim(0,1)
    plt.xlabel("Number of PCs")
    plt.ylabel("Cumulative explained variance")
    plt.legend()
    plt.tight_layout()
    plt.show()


def rolling_r2pca(
    df: pd.DataFrame,
    K: int,
    window_size: int = 12,
    hierarchical: bool = False
) -> tuple[pd.DataFrame, list[np.ndarray], list[float], list[float], R2PCA_I]:
    """
    Run rolling R2‑PCA over trailing windows of size window_size.
    Returns:
      - pc_ts: DataFrame of trailing-window PC scores (rows=date, cols=PC1..PCK)
      - loadings_all: list of loading arrays of shape (K, M)
      - eig_cumvar_list: list of plain PCA cumulative-variance shares in each window
      - r2pca_cumvar_list: list of R2‑PCA reconstruction R² in each window
      - last_model: the final R2PCA_I instance (for inspection)
    """
    from models.embedding.R2PCA import R2PCA_I

    dates = df.index[window_size:]
    scores, score_dates = [], []
    loadings_all = []
    eig_cumvar_list = []
    r2pca_cumvar_list = []
    last_model = None

    for dt in dates:
        win = df.loc[:dt].iloc[-window_size:].copy()
        if win.isna().any().any():
            continue

        # 1) fit R2‑PCA
        mdl = R2PCA_I(n_components=K, pct_variance=None, hierarchical=hierarchical)
        mdl.fit(win, curr_names=list(win.columns))
        last_model = mdl

        # 2) record the last‑month PC scores
        Xr = mdl.transform(win)
        if Xr.ndim == 3:
            Xr = Xr[:, :, 0]
        scores.append(Xr[-1, :K])
        score_dates.append(dt)

        # 3) record the loadings
        loadings_all.append(mdl.prev_eigenvectors_[:K, :])

        # 4) plain‐PCA cumulative variance
        cov = np.cov(win.values, rowvar=False)
        eigs = np.linalg.eigvalsh(cov)[::-1]
        eig_cumvar_list.append(eigs[:K].sum() / eigs.sum())

        # 5) R2‑PCA’s own reconstruction R²
        #    'mdl.current_variance' is set in fit() by accumulating the chosen eigenvalues
        r2pca_cumvar_list.append(float(mdl.current_variance))

    # build the score DataFrame
    pc_ts = pd.DataFrame(
        scores,
        index=score_dates,
        columns=[f"PC{i+1}" for i in range(K)]
    )

    return pc_ts, loadings_all, eig_cumvar_list, r2pca_cumvar_list, last_model



def plot_rolling_scores(
    pc_ts: pd.DataFrame,
    cmap_name: str = "Blues",
    figsize=(12,5)
):
    """Plot pc_ts with PC1 darkest → PCK lightest."""
    K = pc_ts.shape[1]
    cmap = get_cmap(cmap_name)
    plt.figure(figsize=figsize)
    for j in range(K):
        color = cmap(0.3 + 0.7*(K-1-j)/(K-1))
        plt.plot(pc_ts.index, pc_ts.iloc[:,j],
                 label=f"PC{j+1}", color=color, lw=1.5)
    plt.title(f"Rolling PC Scores (PC1→PC{K})")
    plt.xlabel("Date")
    plt.ylabel("Score")
    plt.legend(ncol=2, fontsize="small", loc="upper left")
    plt.tight_layout()
    plt.show()


def select_top_indicators(
    loadings_all: list[np.ndarray],
    feature_names: list[str],
    top_N: int = 8
) -> pd.DataFrame:
    """
    Compute AvgAbsLoading over (windows×components) and return
    a DataFrame sorted desc with columns ['Indicator','AvgAbsLoading'].
    """
    L = np.stack(loadings_all)       # shape (W, K, M)
    avg = np.mean(np.abs(L), axis=(0,1))
    df = pd.DataFrame({
        "Indicator": feature_names,
        "AvgAbsLoading": avg
    }).sort_values("AvgAbsLoading", ascending=False)
    return df


def compute_loading_share(
    loading_df: pd.DataFrame,
    top_n: int = 8
) -> float:
    """
    Returns fraction of total |loading| mass captured by the top_n rows.
    """
    total_mass = loading_df["AvgAbsLoading"].sum()
    top_mass   = loading_df["AvgAbsLoading"].iloc[:top_n].sum()
    return top_mass / total_mass


def get_indicator_metadata(
    meta_df: pd.DataFrame,
    ask_ids: list[str]
) -> pd.DataFrame:
    """
    Retrieve metadata rows for the given ask_ids in their provided order.
    Columns returned: ['ask_id','fed_id','series_name','frequency',
                       'inception_date','units','action'].
    """
    out = meta_df.set_index('ask_id').loc[ask_ids]
    return out.reset_index()

def print_meta_info(
    selected: list[str],
    meta_df: pd.DataFrame
):
    """For each ask_id in selected, print the full meta row as a CSV comment."""
    for ask in selected:
        row = meta_df.loc[meta_df["ask_id"] == ask].iloc[0]
        print(f"# {row['ask_id']},{row['fed_id']},"
              f"\"{row['series_name']}\",{row['frequency']},"
              f"{row['inception_date']},{row['units']},{row['action']}")

