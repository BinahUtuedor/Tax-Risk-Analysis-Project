import pandas as pd

# NEW: config import
from src.config import PROCESSED_DATA_DIR


def create_features(df, save=True):
    """
    Feature engineering step.

    If save=True:
    - saves processed dataset into data/processed/
    """

    df["income_per_year"] = df["declared_income"] / df["years_trading"]

    df["amendments_per_year"] = df["num_amendments"] / df["years_trading"]

    df["filing_risk_index"] = df["late_filings"] + df["num_amendments"]

    # --------------------------------------------------
    # SAVE PROCESSED DATA
    # --------------------------------------------------
    if save:
        processed_path = PROCESSED_DATA_DIR / "taxpayers_processed.csv"
        df.to_csv(processed_path, index=False)
        print(f"[PROCESSED DATA SAVED] {processed_path}")

    return df