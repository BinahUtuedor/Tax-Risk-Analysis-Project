"""
Reporting Module
================

This module generates executive-level outputs:
- Summary report of model performance
- Key business insights
"""

from src.config import REPORT_DIR


# --------------------------------------------------
# EXECUTIVE SUMMARY REPORT
# --------------------------------------------------

def create_summary_report(df, model_name, auc_score):
    """
    Creates a simple executive summary report.

    Outputs:
    - Best performing model
    - AUC score
    - Risk distribution summary
    - Dataset size
    """

    report = f"""
========================================
TAX COMPLIANCE RISK ANALYSIS REPORT
========================================

Best Model:
{model_name}

Model Performance (AUC):
{auc_score:.4f}

----------------------------------------
DATA SUMMARY
----------------------------------------
Total Taxpayers: {len(df)}
High Risk Taxpayers: {(df['risk_band'] == 'High').sum()}
Medium Risk Taxpayers: {(df['risk_band'] == 'Medium').sum()}
Low Risk Taxpayers: {(df['risk_band'] == 'Low').sum()}

----------------------------------------
NOTES
----------------------------------------
- Risk scores are derived from a supervised ML model
- Risk bands are based on probability thresholds
- Explanations are rule-based overlays
"""

    # Save report to run-specific folder
    report_path = REPORT_DIR / "executive_summary.txt"

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)

    return report_path