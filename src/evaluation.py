"""
Evaluation Module
=================

Handles:
- Model evaluation (AUC)
- ROC curve generation
- Confusion matrix plotting
- Feature importance plotting
"""

import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import roc_auc_score, roc_curve, confusion_matrix

from src.config import CHART_DIR


# --------------------------------------------------
# MODEL EVALUATION
# --------------------------------------------------

def evaluate_models(models, X_test, y_test):
    """
    Evaluates all trained models using AUC score.
    Returns dictionary: {model_name: auc_score}
    """

    results = {}

    for name, model in models.items():
        probs = model.predict_proba(X_test)[:, 1]
        results[name] = roc_auc_score(y_test, probs)

    return results


# --------------------------------------------------
# ROC CURVE PLOT
# --------------------------------------------------

def create_roc_curve(model, X_test, y_test):
    """
    Saves ROC curve plot into run/charts/
    """

    probs = model.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, probs)

    plt.figure(figsize=(8, 6))

    plt.plot(fpr, tpr, label="Model ROC")
    plt.plot([0, 1], [0, 1], linestyle="--", label="Random Guess")

    plt.title("ROC Curve")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.legend()

    plt.tight_layout()
    plt.savefig(CHART_DIR / "roc_curve.png")
    plt.close()


# --------------------------------------------------
# CONFUSION MATRIX PLOT
# --------------------------------------------------

def create_confusion_matrix(model, X_test, y_test):
    """
    Saves confusion matrix plot into run/charts/
    """

    preds = model.predict(X_test)
    cm = confusion_matrix(y_test, preds)

    plt.figure(figsize=(6, 5))

    plt.imshow(cm, cmap="Blues")
    plt.title("Confusion Matrix")
    plt.colorbar()

    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    plt.tight_layout()
    plt.savefig(CHART_DIR / "confusion_matrix.png")
    plt.close()


# --------------------------------------------------
# FEATURE IMPORTANCE PLOT (NEW FIX)
# --------------------------------------------------

def create_feature_importance(model, feature_names):
    """
    Creates feature importance plot for:
    - Random Forest (feature_importances_)
    - Logistic Regression (coef_)

    Saves output into run/charts/feature_importance.png
    """

    # --------------------------------------------------
    # EXTRACT IMPORTANCE VALUES
    # --------------------------------------------------

    if hasattr(model, "feature_importances_"):
        importances = model.feature_importances_

    elif hasattr(model, "coef_"):
        importances = model.coef_[0]

    else:
        raise ValueError("Model does not support feature importance")

    # --------------------------------------------------
    # SORT FEATURES BY IMPORTANCE
    # --------------------------------------------------

    indices = np.argsort(importances)

    sorted_features = [feature_names[i] for i in indices]
    sorted_importances = importances[indices]

    # --------------------------------------------------
    # PLOT
    # --------------------------------------------------

    plt.figure(figsize=(10, 6))

    plt.barh(sorted_features, sorted_importances)

    plt.title("Feature Importance")
    plt.xlabel("Importance")

    plt.tight_layout()

    plt.savefig(CHART_DIR / "feature_importance.png")
    plt.close()