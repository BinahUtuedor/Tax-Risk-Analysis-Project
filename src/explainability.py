"""
SHAP explainability module.

Generates:
- SHAP beeswarm plot
"""

import shap
import matplotlib.pyplot as plt

from src.config import CHART_DIR


def generate_shap_plot(model, X_train):
    """
    Saves SHAP beeswarm plot into run/charts/
    """

    explainer = shap.Explainer(model, X_train)
    shap_values = explainer(X_train)

    shap.plots.beeswarm(shap_values, show=False)

    plt.tight_layout()
    plt.savefig(CHART_DIR / "shap_beeswarm.png")
    plt.close()