import numpy as np
import pandas as pd

# NEW: import config paths
from src.config import RAW_DATA_DIR


def generate_taxpayer_data(n=2000, save=True):
    """
    Generates synthetic taxpayer dataset.

    If save=True:
    - stores raw dataset in data/raw/
    """

    declared_income = np.random.lognormal(mean=10.5, sigma=0.6, size=n)

    expense_ratio = np.clip(np.random.beta(2, 5, n), 0.01, 0.90)

    years_trading = np.random.randint(1, 30, n)

    num_amendments = np.random.poisson(0.4, n)

    offshore_flag = np.random.binomial(1, 0.08, n)

    late_filings = np.random.poisson(0.3, n)

    sector_risk = np.random.choice([0, 1, 2], n, p=[0.6, 0.3, 0.1])

    log_odds = (
        -4
        + 0.0001 * declared_income
        + 3.0 * expense_ratio
        - 0.04 * years_trading
        + 0.5 * num_amendments
        + 1.8 * offshore_flag
        + 0.4 * late_filings
        + 0.7 * sector_risk
        + np.random.normal(0, 0.5, n)
    )

    prob = 1 / (1 + np.exp(-log_odds))
    non_compliant = (prob > 0.5).astype(int)

    df = pd.DataFrame({
        "declared_income": declared_income,
        "expense_ratio": expense_ratio,
        "years_trading": years_trading,
        "num_amendments": num_amendments,
        "offshore_flag": offshore_flag,
        "late_filings": late_filings,
        "sector_risk": sector_risk,
        "non_compliant": non_compliant
    })

    # --------------------------------------------------
    # SAVE RAW DATA
    # --------------------------------------------------
    if save:
        raw_path = RAW_DATA_DIR / "taxpayers_raw.csv"
        df.to_csv(raw_path, index=False)
        print(f"[RAW DATA SAVED] {raw_path}")

    return df