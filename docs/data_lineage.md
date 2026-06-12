# Data Lineage

## Overview

This document describes how data flows through the Tax Risk Scoring Project from initial generation to final reporting outputs.

The objective is to provide transparency, traceability, and reproducibility across the analytical workflow.

---

# End-to-End Data Flow

```text
Synthetic Data Generation
            ↓
Raw Dataset Storage
            ↓
Feature Engineering
            ↓
Processed Dataset Storage
            ↓
Data Preparation
            ↓
Train/Test Split
            ↓
Feature Scaling
            ↓
Model Training
            ↓
Model Evaluation
            ↓
Best Model Selection
            ↓
Risk Score Generation
            ↓
Risk Band Assignment
            ↓
Risk Explanation Engine
            ↓
Explainability Outputs
            ↓
Executive Reporting
            ↓
Model Persistence
            ↓
Metadata Capture
```

---

# Lineage Stages

## Stage 1: Synthetic Data Generation

### Module

```text
src/data_generation.py
```

### Function

```python
generate_taxpayer_data()
```

### Inputs

* Random seed
* Taxpayer sample size

### Outputs

```text
data/raw/taxpayers_raw.csv
```

### Purpose

Creates synthetic taxpayer records for modelling.

---

## Stage 2: Feature Engineering

### Module

```text
src/feature_engineering.py
```

### Function

```python
create_features()
```

### Inputs

```text
data/raw/taxpayers_raw.csv
```

### Outputs

```text
data/processed/taxpayers_processed.csv
```

### Derived Variables

* income_per_year
* amendments_per_year
* filing_risk_index

---

## Stage 3: Data Preparation

### Module

```text
src/preprocessing.py
```

### Activities

* Feature selection
* Train/test split
* Standardisation
* Scaler creation

### Outputs

* X_train
* X_test
* y_train
* y_test
* scaler.pkl

---

## Stage 4: Model Training

### Module

```text
src/modelling.py
```

### Models Trained

* Logistic Regression
* Random Forest

### Outputs

Trained model objects.

---

## Stage 5: Model Evaluation

### Module

```text
src/evaluation.py
```

### Metrics

* ROC-AUC

### Artefacts Produced

```text
roc_curve.png
confusion_matrix.png
feature_importance.png
```

### Purpose

Identify the best-performing model.

---

## Stage 6: Best Model Selection

### Selection Rule

```text
Highest ROC-AUC Score
```

### Output

Best model promoted to production outputs.

---

## Stage 7: Risk Scoring

### Module

```text
src/risk_scoring.py
```

### Activity

Generate predicted probabilities.

### Output Variable

```text
risk_score
```

---

## Stage 8: Risk Categorisation

### Rules

| Risk Band | Probability Range |
| --------- | ----------------- |
| Low       | 0.00–0.30         |
| Medium    | 0.30–0.60         |
| High      | 0.60–1.00         |

### Output

```text
risk_band
```

---

## Stage 9: Explanation Layer

### Methods

#### Rule-Based Explanations

Potential triggers:

* Offshore Account
* High Expense Ratio
* Repeated Late Filings
* Frequent Amendments

#### SHAP Explainability

Produces:

```text
shap_beeswarm.png
```

---

## Stage 10: Reporting

### Module

```text
src/reporting.py
```

### Outputs

```text
executive_summary.txt
taxpayer_scores.csv
high_risk_taxpayers.csv
```

### Purpose

Provide decision-ready outputs.

---

## Stage 11: Model Persistence

### Outputs

```text
risk_model.pkl
scaler.pkl
```

### Purpose

Support reproducibility and future deployment.

---

## Stage 12: Metadata and Audit Trail

### Output

```text
metadata.json
```

### Captured Information

* Best model selected
* ROC-AUC score
* Number of samples
* Number of features

### Purpose

Enable auditability and run traceability.

---

# Output Directory Structure

```text
outputs/
└── run_YYYY-MM-DD_HH-MM-SS/
    ├── charts/
    ├── reports/
    ├── models/
    └── metadata.json
```

Each execution creates a unique timestamped folder, ensuring that all analytical artefacts remain versioned and reproducible.

---

# Governance Considerations

* Synthetic data only.
* No personally identifiable information is processed.
* All outputs are reproducible through timestamped runs.
* Model selection is evidence-based using ROC-AUC.
* Explainability mechanisms improve transparency of risk decisions.

---

# Disclaimer

This lineage document represents the flow of a demonstration project using synthetic data and does not reflect operational procedures of any tax authority.
