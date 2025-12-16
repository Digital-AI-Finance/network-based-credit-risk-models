# r2rd_utils.py

import pandas as pd
import numpy as np
from collections import deque
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from models.HMMs.r2_gaussian_hmm import R2GaussianHMM
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


__all__ = [
    "prepare_regime_data",
    "compute_bic_scores",
    "select_best_k",
    "plot_bic_scores",
    "warm_start_hmm",
    "rolling_oos_ll",
    "compute_cv_scores",
    "select_best_k_cv",
    "select_best_k_combined",
    "plot_cv_scores"


]

def prepare_regime_data(
    df_final: pd.DataFrame,
    ask_ids: list[str],
    impute_date: str,
    scale_method: str = "none"
) -> tuple[pd.DataFrame, object|None]:
    """
    1) Subset df_final to the selected indicators,
    2) linearly interpolate any gaps after impute_date,
    3) apply scaling ('none','zscore','minmax','robust').
    Returns (df_scaled_regime, fitted_scaler).
    """
    # 1) subset
    df = df_final[ask_ids].copy()

    # 2) interpolate after impute_date
    mask = df.index > pd.to_datetime(impute_date)
    df.loc[mask] = df.loc[mask].interpolate(method="linear")

    # 3) scale
    scalers = {
        "none":   None,
        "zscore": StandardScaler(),
        "minmax": MinMaxScaler(),
        "robust": RobustScaler(),
    }
    scaler = scalers.get(scale_method)
    if scaler is not None:
        arr = scaler.fit_transform(df.values)
        df = pd.DataFrame(arr, index=df.index, columns=df.columns)

    return df, scaler

def compute_bic_scores(
    df_scaled_regime: pd.DataFrame,
    train_end: str,
    k_min: int = 2,
    k_max: int = 10
) -> dict[int,float]:
    """
    Fit R2GaussianHMM for k in [k_min..k_max] on the slice up to train_end,
    compute BIC_k = -2*LL + p*ln(N). Returns {k: BIC_k}.
    """
    data = df_scaled_regime.loc[:train_end].values
    N, d = data.shape

    def num_params(k,d): 
        return (k-1) + k*(k-1) + 2*k*d

    bic_scores = {}
    for k in range(k_min, k_max+1):
        model_k = R2GaussianHMM(n_components=k, n_iter=1000, tol=1e-5)
        model_k.fit(data)
        ll  = model_k.model.score(data)
        p   = num_params(k, d)
        bic = -2 * ll + p * math.log(N)
        bic_scores[k] = bic

    return bic_scores

def select_best_k(bic_scores: dict[int,float]) -> int:
    """Return k that minimizes BIC."""
    return min(bic_scores, key=bic_scores.get)

def plot_bic_scores(bic_scores: dict[int,float]) -> None:
    import matplotlib.pyplot as plt
    ks = list(bic_scores.keys())
    vals = [bic_scores[k] for k in ks]
    plt.figure(figsize=(8,5))
    plt.plot(ks, vals, marker="o")
    plt.xlabel("Number of Regimes")
    plt.ylabel("BIC Score")
    plt.title("BIC Model Selection")
    plt.tight_layout()
    plt.show()

def warm_start_hmm(
    df_scaled_regime: pd.DataFrame,
    K: int,
    start_length: int = 24
) -> tuple[pd.DataFrame, R2GaussianHMM]:
    """
    1) Warm‑up fit on first start_length observations,
    2) Rolling re‑fit (warm start) and one‑step smoothing:
       produce posterior P1..PK and decoded RegimeLabel.
    Returns (df_probs, fitted_model).
    """
    model = R2GaussianHMM(n_components=K, n_iter=1000, tol=1e-5)

    # warm‑up
    warm_X = df_scaled_regime.iloc[:start_length].values
    model.fit(warm_X)

    from collections import deque
    import numpy as np

    # rolling inference
    records = []
    cost_buffer = deque([-model.model.score(x.reshape(1,-1)) 
                         for x in warm_X[-12:]], maxlen=12)

    for t in df_scaled_regime.index[start_length:]:
        chunk = df_scaled_regime.loc[:t].values
        model.fit(chunk)  # warm‑start
        post = model.transform(chunk)
        probs = post[-1] if not hasattr(post, "iloc") else post.iloc[-1].values
        label = int(np.argmax(probs)) + 1
        records.append({**{f"P{i+1}": probs[i] for i in range(K)},
                        "RegimeLabel": label,
                        "Date": t})
        # update cost buffer (optional surprise detection)
        cost_buffer.append(-model.model.score(chunk[-1].reshape(1,-1)))

    df_probs = pd.DataFrame(records).set_index("Date")
    return df_probs, model

def get_regime_change_dates(
    df_probs: pd.DataFrame,
    label_col: str = 'RegimeLabel'
) -> pd.DatetimeIndex:
    """Return the dates where the regime label changes."""
    return df_probs.index[df_probs[label_col] != df_probs[label_col].shift(1)]


def plot_regime_labels(
    df_probs: pd.DataFrame,
    K: int,
    label_col: str = 'RegimeLabel',
    figsize: tuple[int,int] = (12,4)
) -> None:
    """
    Step‐plot of regime labels with vertical lines at change dates.
    """
    change_dates = get_regime_change_dates(df_probs, label_col)
    fig, ax = plt.subplots(figsize=figsize)
    ax.step(df_probs.index, df_probs[label_col], where='post', lw=1, marker='o')
    for d in change_dates:
        ax.axvline(d, color='red', linestyle='--', alpha=0.7)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_title(f"Final Regime Labels (K={K})")
    ax.set_xlabel("Date")
    ax.set_ylabel("Regime")
    plt.tight_layout()
    plt.show()

    # -----------------------------------------------------------------------------
# STEP 2.3.5: Rolling‑Window CV for K Selection & Combine with BIC
# -----------------------------------------------------------------------------

def rolling_oos_ll(
    df_scaled_regime: pd.DataFrame,
    k: int,
    initial_train: str,
    test_horizon: int = 12,
    step: int = 12
) -> float:
    """
    Train HMM with `k` states on data up to each fold point, then test on the next
    `test_horizon` observations. Slides forward by `step`. Returns mean cum‑LL.
    """
    # find first index location on or after initial_train
    initial_dt = pd.to_datetime(initial_train)
    idx0 = df_scaled_regime.index.searchsorted(initial_dt)
    n   = len(df_scaled_regime)
    oos_lls = []
    for start in range(idx0, n - test_horizon, step):
        train_arr = df_scaled_regime.iloc[:start].values
        test_arr  = df_scaled_regime.iloc[start:start+test_horizon].values

        mdl = R2GaussianHMM(n_components=k, n_iter=500, tol=1e-4)
        mdl.fit(train_arr)

        # sum per‑point log‑likelihood on test window
        ll = sum(mdl.model.score(x.reshape(1,-1)) for x in test_arr)
        oos_lls.append(ll)

    return np.mean(oos_lls)


def compute_cv_scores(
    df_scaled_regime: pd.DataFrame,
    k_min: int,
    k_max: int,
    initial_train: str,
    test_horizon: int = 12,
    step: int = 12
) -> dict[int, float]:
    """
    Compute rolling-window CV OOS cumulative LL for k in [k_min..k_max].
    """
    return {
        k: rolling_oos_ll(
            df_scaled_regime,
            k,
            initial_train=initial_train,
            test_horizon=test_horizon,
            step=step
        )
        for k in range(k_min, k_max + 1)
    }


def select_best_k_cv(cv_scores: dict[int, float]) -> int:
    """
    Return k that maximizes the CV cumulative LL.
    """
    return max(cv_scores, key=cv_scores.get)


def select_best_k_combined(
    best_k_bic: int,
    best_k_cv: int,
    cv_scores: dict[int, float]
) -> int:
    """
    Combine BIC and CV choices: if they agree, return that; otherwise pick the one
    with the higher CV LL on its own window.
    """
    if best_k_bic == best_k_cv:
        return best_k_bic
    bic_ll = cv_scores.get(best_k_bic, -np.inf)
    cv_ll  = cv_scores.get(best_k_cv,  -np.inf)
    return best_k_cv if cv_ll >= bic_ll else best_k_bic


def plot_cv_scores(
    cv_scores: dict[int, float],
    best_k_final: int,
    figsize: tuple[int,int] = (6,3)
) -> None:
    """
    Plot CV scores and highlight the final chosen K.
    """
    ks  = sorted(cv_scores.keys())
    lls = [cv_scores[k] for k in ks]
    plt.figure(figsize=figsize)
    plt.plot(ks, lls, marker='o', label='CV LL')
    plt.scatter([best_k_final], [cv_scores[best_k_final]], color='red',
                zorder=5, label=f'Final K={best_k_final}')
    plt.xlabel('Number of Regimes (K)')
    plt.ylabel('Mean OOS Cumulative LL')
    plt.title('Rolling-Window CV for HMM K Selection')
    plt.legend()
    plt.tight_layout()
    plt.show()