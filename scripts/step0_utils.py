import pandas as pd
import csv
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from matplotlib.cm import get_cmap
from models.embedding.R2PCA import R2PCA_I

__all__ = [
    "compute_full_sample_r2pca", "determine_fixed_k", "plot_scree",  
    "rolling_r2pca", "plot_rolling_pc_scores", "select_top_indicators",
    "get_indicator_metadata", "load_macro_data", "load_metadata",
    "audit_metadata_coverage"
]

def load_macro_data(path: str) -> pd.DataFrame:
    """Load Parquet, parse index as datetime."""
    df = pd.read_parquet(path)
    df.index = pd.to_datetime(df.index)
    return df

def load_metadata(path: str) -> pd.DataFrame:
    """Load metadata CSV and strip whitespace from column names."""
    md = pd.read_csv(path)
    md.columns = md.columns.str.strip()
    return md

def maybe_stationarize(col_series, action, diff=True):
    if action in ('diff','pct'):
        return col_series.dropna()
    # otherwise run your ADF + optional differencing
    pv = adfuller(col_series.dropna())[1]
    if pv < 0.05 or not diff:
        return col_series.dropna()
    return col_series.diff().dropna()

def audit_metadata_coverage(
    meta_df: pd.DataFrame,
    category_keywords: dict[str, list[str]]
) -> pd.DataFrame:
    """
    Given full metadata and a mapping of categories to keyword lists,
    returns a DataFrame showing, for each category:
      - Covered? (bool): whether any series_name contains any keyword
      - Example Series: up to 3 matching series_name values
    """
    rows = []
    series_lower = meta_df["series_name"].str.lower()
    for category, kws in category_keywords.items():
        mask = series_lower.apply(lambda s: any(kw.lower() in s for kw in kws))
        examples = meta_df.loc[mask, "series_name"].head(3).tolist()
        rows.append({
            "Category":      category,
            "Covered?":      bool(mask.any()),
            "Example Series": examples
        })
    return pd.DataFrame(rows)

def compute_full_sample_r2pca(
    df: pd.DataFrame,
    pct_variance: float = 0.75,
    hierarchical: bool = False
) -> tuple[R2PCA_I, np.ndarray, float, np.ndarray]:
    """
    Fit full-sample R2-PCA to df, return model, eigenvalues, total variance, and explained ratios.
    """
    model = R2PCA_I(pct_variance=pct_variance, hierarchical=hierarchical)
    model.fit(df, curr_names=list(df.columns))
    eigs = np.real(model.val)
    total_var = model.total_var
    ratios = eigs / total_var
    return model, eigs, total_var, ratios


def determine_fixed_k(
    ratios: np.ndarray,
    pct_target: float = 0.75,
    fixed_k: int | None = None
) -> tuple[int, float]:
    """
    Either use provided fixed_k or choose the smallest K explaining >=pct_target.
    Returns (K, cumvar_at_K).
    """
    if fixed_k is None:
        cum = np.cumsum(ratios)
        K = int(np.searchsorted(cum, pct_target) + 1)
        cumvar = cum[K-1]
    else:
        cumvar = ratios[:fixed_k].sum()
        K = fixed_k
    return K, cumvar


def plot_scree(
    ratios: np.ndarray,
    fixed_k: int,
    pct_target: float = 0.75,
    n_max: int = 20
) -> None:
    """
    Plot cumulative explained variance up to n_max PCs, mark fixed_k and pct_target.
    """
    cum = np.cumsum(ratios)
    plt.figure(figsize=(6,4))
    plt.plot(np.arange(1, len(cum)+1), cum, marker="o")
    plt.axvline(fixed_k, color="gray", ls="--", label=f"PC{fixed_k} cutoff")
    plt.axhline(pct_target, color="red", ls="--", label=f"{int(pct_target*100)}% target")
    plt.xlim(1, min(n_max, len(cum)))
    plt.ylim(0,1)
    plt.xlabel("Number of PCs")
    plt.ylabel("Cumulative explained variance")
    plt.legend()
    plt.tight_layout()
    plt.show()

def impute_after_date(df, start_date):
    """
    For rows with index (dates) > start_date, interpolate using a linear method.
    """
    df = df.copy()
    df.index = pd.to_datetime(df.index)
    mask = df.index > pd.to_datetime(start_date)
    df.loc[mask] = df.loc[mask].interpolate(method='linear')
    return df

def rolling_r2pca(
    df: pd.DataFrame,
    K: int,
    window_size: int = 12,
    hierarchical: bool = False
) -> tuple[pd.DataFrame, list[np.ndarray], list[float]]:
    """
    Perform rolling-window R2-PCA and return pc_ts, loadings list, and cumvar list.
    """
    dates = df.index[window_size:]
    scores, loadings_all, cumvars = [], [], []
    score_dates = []
    for dt in dates:
        win = df.loc[:dt].iloc[-window_size:].copy()
        win.replace([np.inf, -np.inf], np.nan, inplace=True)
        win.ffill().bfill(inplace=True)
        if win.isna().any().any():
            continue
        mdl = R2PCA_I(n_components=K, pct_variance=None, hierarchical=hierarchical)
        mdl.fit(win, curr_names=list(win.columns))
        Xr = mdl.transform(win)
        if Xr.ndim == 3:
            Xr = Xr[:, :, 0]
        scores.append(Xr[-1, :K])
        loadings_all.append(mdl.prev_eigenvectors_[:K, :])
        score_dates.append(dt)
        cov = np.cov(win.values, rowvar=False)
        eigs = np.sort(np.linalg.eigvalsh(cov))[::-1]
        cumvars.append(eigs[:K].sum() / eigs.sum())
    pc_ts = pd.DataFrame(
        scores, index=score_dates, columns=[f"PC{i+1}" for i in range(K)]
    )
    return pc_ts, loadings_all, cumvars


def plot_rolling_pc_scores(
    pc_ts: pd.DataFrame,
    cmap_name: str = "Blues"
) -> None:
    """
    Plot the rolling PC scores with a color gradient.
    """
    K = pc_ts.shape[1]
    cmap = get_cmap(cmap_name)
    plt.figure(figsize=(12,5))
    for j in range(K):
        color = cmap(0.3 + 0.7*(K-1-j)/(K-1))
        plt.plot(pc_ts.index, pc_ts.iloc[:, j], label=f"PC{j+1}",
                 color=color, lw=1.5)
    plt.title(f"Rolling PC Scores (PC1 → PC{K})")
    plt.xlabel("Date")
    plt.ylabel("Score")
    plt.legend(ncol=2, fontsize="small", loc="upper left")
    plt.tight_layout()
    plt.show()


def select_top_indicators(
    loadings_all: list[np.ndarray],
    columns: list[str],
    top_n: int = 8
) -> tuple[pd.DataFrame, list[str]]:
    """
    Compute avg absolute loading over windows and return sorted DataFrame and top_n list.
    """
    L = np.stack(loadings_all)
    avgL = np.mean(np.abs(L), axis=(0,1))
    df = pd.DataFrame({"Indicator": columns, "AvgAbsLoading": avgL})
    df = df.sort_values("AvgAbsLoading", ascending=False).reset_index(drop=True)
    return df, df.Indicator.iloc[:top_n].tolist()


def get_indicator_metadata(
    meta_df: pd.DataFrame,
    ask_ids: list[str]
) -> pd.DataFrame:
    """
    Retrieve full metadata rows for given ask_ids in original order.
    """
    return meta_df.set_index('ask_id').loc[ask_ids].reset_index()

def filter_metadata_by_keywords(meta_df: pd.DataFrame, keywords: list[str]) -> pd.DataFrame:
    mask = (
        meta_df["series_name"]
        .str.lower()
        .apply(lambda s: any(kw.lower() in s for kw in keywords))
    )
    return meta_df[mask].copy()

def subset_macro_by_ask_ids(macro_df: pd.DataFrame, ask_ids: list[str]) -> pd.DataFrame:
    common = list(set(macro_df.columns) & set(ask_ids))
    return macro_df[common].copy()

def convert_to_numeric(df: pd.DataFrame) -> pd.DataFrame:
    return df.apply(pd.to_numeric, errors="coerce")

def filter_by_date(df: pd.DataFrame, start_date: str) -> pd.DataFrame:
    return df[df.index >= pd.to_datetime(start_date)]

def plot_missing_data_heatmap(df: pd.DataFrame, **kwargs) -> None:
    plt.figure(**{k: v for k, v in kwargs.items() if k in ("figsize","dpi")})
    sns.heatmap(df.isna(), cbar=False, yticklabels=False)
    plt.xlabel("Series"); plt.ylabel("Date")
    plt.show()

def fill_missing_two_way(df: pd.DataFrame) -> pd.DataFrame:
    return df.ffill().bfill()

def impute_after_date(df: pd.DataFrame, start_date: str) -> pd.DataFrame:
    out = df.copy()
    mask = out.index > pd.to_datetime(start_date)
    out.loc[mask] = out.loc[mask].interpolate(method="linear")
    return out

def prune_correlated(df: pd.DataFrame, threshold: float = 0.9):
    corr = df.corr().abs().round(3)
    to_drop = set()
    cols = corr.columns
    for i in range(len(cols)):
        for j in range(i):
            if corr.iloc[i,j] > threshold:
                to_drop.add(cols[i])
    return df.drop(columns=sorted(to_drop)), sorted(to_drop)

def scale_df(df: pd.DataFrame, method: str = "none"):
    scalers = {
        "none":   None,
        "zscore": StandardScaler(),
        "minmax": MinMaxScaler(),
        "robust": RobustScaler()
    }
    scaler = scalers.get(method)
    if scaler is None:
        return df.copy(), None
    arr = scaler.fit_transform(df)
    return pd.DataFrame(arr, index=df.index, columns=df.columns), scaler

def maybe_stationarize(col: pd.Series, action: str, diff: bool = True) -> pd.Series:
    if action in ("diff","pct"):
        return col.dropna()
    pval = round(adfuller(col.dropna())[1], 3)
    if pval < 0.05 or not diff:
        return col.dropna()
    return col.diff().dropna()

def stationarize_df(df: pd.DataFrame, action_map: dict[str,str], diff: bool = True):
    out = {}
    for col in df.columns:
        act = action_map.get(col, "none")
        out[col] = maybe_stationarize(df[col], act, diff=diff)
    return pd.DataFrame(out).dropna(how="any")
