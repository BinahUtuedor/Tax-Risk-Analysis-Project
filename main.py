"""
Main Pipeline Orchestrator
==========================

Runs full tax risk scoring workflow:
1. Data generation
2. Feature engineering
3. Model training
4. Evaluation
5. Risk scoring
6. Explainability
7. Reporting
8. Saving outputs
"""

# --------------------------------------------------
# IMPORTS
# --------------------------------------------------

import joblib
import json

from src.config import MODEL_DIR, REPORT_DIR, RUN_DIR

from src.data_generation import generate_taxpayer_data
from src.feature_engineering import create_features
from src.preprocessing import prepare_data
from src.modelling import train_models

from src.evaluation import (
    evaluate_models,
    create_roc_curve,
    create_confusion_matrix,
    create_feature_importance
)

from src.risk_scoring import (
    assign_risk_bands,
    generate_risk_reason,
    plot_risk_distribution
)

from src.reporting import create_summary_report

from src.explainability import generate_shap_plot


# --------------------------------------------------
# STEP 1: DATA GENERATION
# --------------------------------------------------

print("\n[1] Generating synthetic data...")

df = generate_taxpayer_data(save=True)

print(f"Dataset size: {len(df):,}")


# --------------------------------------------------
# STEP 2: FEATURE ENGINEERING
# --------------------------------------------------

print("\n[2] Feature engineering...")

df = create_features(df, save=True)


# --------------------------------------------------
# STEP 3: FEATURES LIST
# --------------------------------------------------

features = [
    "declared_income",
    "expense_ratio",
    "years_trading",
    "num_amendments",
    "offshore_flag",
    "late_filings",
    "sector_risk",
    "income_per_year",
    "amendments_per_year",
    "filing_risk_index"
]


# --------------------------------------------------
# STEP 4: TRAIN/TEST SPLIT
# --------------------------------------------------

print("\n[3] Preparing data...")

X_train, X_test, y_train, y_test, scaler = prepare_data(df, features)


# --------------------------------------------------
# STEP 5: MODEL TRAINING
# --------------------------------------------------

print("\n[4] Training models...")

models = train_models(X_train, y_train)


# --------------------------------------------------
# STEP 6: MODEL EVALUATION
# --------------------------------------------------

print("\n[5] Evaluating models...")

results = evaluate_models(models, X_test, y_test)

for name, auc in results.items():
    print(f"{name:<20} AUC: {auc:.4f}")


# --------------------------------------------------
# STEP 7: SELECT BEST MODEL
# --------------------------------------------------

best_model_name = max(results, key=results.get)
best_model = models[best_model_name]
best_auc = results[best_model_name]

print("\nBest Model Selected:", best_model_name)


# --------------------------------------------------
# STEP 8: RISK SCORES
# --------------------------------------------------

print("\n[6] Generating risk scores...")

df["risk_score"] = best_model.predict_proba(
    scaler.transform(df[features])
)[:, 1]


# --------------------------------------------------
# STEP 9: RISK BANDS
# --------------------------------------------------

print("\n[7] Assigning risk bands...")

df = assign_risk_bands(df)


# --------------------------------------------------
# STEP 10: EXPLANATIONS
# --------------------------------------------------

print("\n[8] Generating explanations...")

df["risk_reason"] = df.apply(generate_risk_reason, axis=1)


# --------------------------------------------------
# STEP 11: CHARTS
# --------------------------------------------------

print("\n[9] Generating charts...")

create_roc_curve(best_model, X_test, y_test)
create_confusion_matrix(best_model, X_test, y_test)
plot_risk_distribution(df)
generate_shap_plot(best_model, scaler.transform(df[features]))

# NEW: FEATURE IMPORTANCE
create_feature_importance(best_model, features)


# --------------------------------------------------
# STEP 12: REPORTING
# --------------------------------------------------

print("\n[10] Generating report...")

report_path = create_summary_report(df, best_model_name, best_auc)


# --------------------------------------------------
# STEP 13: EXPORT DATA
# --------------------------------------------------

print("\n[11] Exporting datasets...")

df.to_csv(REPORT_DIR / "taxpayer_scores.csv", index=False)

df[df["risk_band"] == "High"].to_csv(
    REPORT_DIR / "high_risk_taxpayers.csv",
    index=False
)


# --------------------------------------------------
# STEP 14: SAVE MODELS
# --------------------------------------------------

print("\n[12] Saving models...")

joblib.dump(best_model, MODEL_DIR / "risk_model.pkl")
joblib.dump(scaler, MODEL_DIR / "scaler.pkl")


# --------------------------------------------------
# STEP 15: METADATA
# --------------------------------------------------

metadata = {
    "best_model": best_model_name,
    "auc_score": float(best_auc),
    "n_samples": len(df),
    "n_features": len(features)
}

with open(RUN_DIR / "metadata.json", "w") as f:
    json.dump(metadata, f, indent=4)


# --------------------------------------------------
# PIPELINE COMPLETE
# --------------------------------------------------

print("\n===================================")
print("PIPELINE COMPLETED SUCCESSFULLY")
print("===================================")
print(f"Results saved in: {RUN_DIR}")