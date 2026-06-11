"""
Risk Scoring Module
====================

This module handles:
- Converting predicted probabilities into risk bands
- Generating human-readable risk explanations
- Plotting risk score distributions
"""

import pandas as pd
import matplotlib.pyplot as plt

from src.config import CHART_DIR


# --------------------------------------------------
# RISK BAND ASSIGNMENT
# --------------------------------------------------

def assign_risk_bands(df):
    """
    Converts continuous risk scores into categorical bands.

    Bands:
    - Low: 0.0 - 0.3
    - Medium: 0.3 - 0.6
    - High: 0.6 - 1.0
    """

    df["risk_band"] = pd.cut(
        df["risk_score"],
        bins=[0, 0.3, 0.6, 1.0],
        labels=["Low", "Medium", "High"]
    )

    return df


# --------------------------------------------------
# RISK EXPLANATION ENGINE
# --------------------------------------------------

def generate_risk_reason(row):
    """
    Generates explainable reasoning for why a taxpayer is high risk.

    This is a rule-based explanation layer on top of ML predictions.
    """

    reasons = []

    if row.get("offshore_flag", 0) == 1:
        reasons.append("Offshore Account")

    if row.get("expense_ratio", 0) > 0.60:
        reasons.append("High Expense Ratio")

    if row.get("late_filings", 0) > 2:
        reasons.append("Repeated Late Filings")

    if row.get("num_amendments", 0) > 3:
        reasons.append("Frequent Amendments")

    return "; ".join(reasons)


# --------------------------------------------------
# RISK SCORE DISTRIBUTION PLOT
# --------------------------------------------------

def plot_risk_distribution(df):
    """
    Creates histogram of risk scores across all taxpayers.

    Helps visualize:
    - Model separation quality
    - Risk concentration
    """

    plt.figure(figsize=(8, 5))

    df["risk_score"].hist(
        bins=30,
        edgecolor="black"
    )

    plt.title("Risk Score Distribution")
    plt.xlabel("Risk Score")
    plt.ylabel("Number of Taxpayers")

    plt.tight_layout()
    plt.savefig(CHART_DIR / "risk_distribution.png")
    plt.close()