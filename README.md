# Tax Risk Scoring Project

## Overview

The **Tax Risk Scoring Project** is an end-to-end machine learning pipeline designed to identify potentially non-compliant taxpayers using predictive analytics and explainable AI techniques.

The project simulates a real-world tax authority risk assessment process by generating synthetic taxpayer data, engineering features, training multiple classification models, assigning risk scores, producing explainability outputs, and generating executive-level reports.

The solution demonstrates best practices in:

* Machine Learning Operations (MLOps)
* Risk Analytics
* Explainable AI (XAI)
* Data Engineering
* Automated Reporting
* Reproducible Data Science

---

## Objectives

The project aims to:

* Generate realistic synthetic taxpayer datasets.
* Identify taxpayers with a high probability of non-compliance.
* Compare multiple machine learning algorithms.
* Produce interpretable risk scores.
* Provide transparent explanations for risk classifications.
* Generate executive-ready outputs for decision makers.
* Save all artefacts in timestamped run folders for reproducibility.

---

## Key Features

### Synthetic Data Generation

Generates taxpayer records including:

* Declared income
* Expense ratios
* Trading history
* Filing behaviour
* Offshore account indicators
* Amendment frequency
* Sector risk categories

---

### Feature Engineering

Creates additional predictive variables such as:

* Income per trading year
* Amendments per year
* Filing risk index

---

### Machine Learning Models

The pipeline trains and evaluates multiple models:

* Logistic Regression
* Random Forest Classifier

The best-performing model is automatically selected using ROC-AUC.

---

### Risk Scoring

Each taxpayer receives a probability-based risk score.

Risk bands are assigned as follows:

| Risk Band | Probability Range |
| --------- | ----------------- |
| Low       | 0.00 – 0.30       |
| Medium    | 0.30 – 0.60       |
| High      | 0.60 – 1.00       |

---

### Explainable AI

The project improves transparency through:

#### SHAP Explainability

Generates SHAP beeswarm visualisations showing how features influence predictions.

#### Rule-Based Explanations

Provides human-readable reasons for elevated risk, including:

* Offshore Account
* High Expense Ratio
* Repeated Late Filings
* Frequent Amendments

---

### Executive Reporting

Automatically generates:

* Executive summary reports
* Taxpayer risk registers
* High-risk taxpayer extracts
* Metadata for auditability

---

## Project Structure

```text
tax_risk_scoring_project/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── outputs/
│   └── run_YYYY-MM-DD_HH-MM-SS/
│       ├── charts/
│       ├── reports/
│       ├── models/
│       └── metadata.json
│
├── src/
│   ├── config.py
│   ├── data_generation.py
│   ├── feature_engineering.py
│   ├── preprocessing.py
│   ├── modelling.py
│   ├── evaluation.py
│   ├── explainability.py
│   ├── risk_scoring.py
│   └── reporting.py
│
├── docs/
│   ├── data_dictionary.md
│   └── data_lineage.md
│
├── requirements.txt
├── README.md
└── main.py
```

---

## Pipeline Workflow

```text
Synthetic Data
      ↓
Feature Engineering
      ↓
Preprocessing
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Best Model Selection
      ↓
Risk Scoring
      ↓
Risk Band Assignment
      ↓
Explainability
      ↓
Executive Reporting
      ↓
Artefact Persistence
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/tax-risk-scoring-project.git

cd tax-risk-scoring-project
```

---

### Create a Virtual Environment

#### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

#### macOS/Linux

```bash
python -m venv venv

source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Pipeline

Execute the full workflow:

```bash
python main.py
```

Example console output:

```text
[1] Generating synthetic data...
[2] Feature engineering...
[3] Preparing data...
[4] Training models...
[5] Evaluating models...
[6] Generating risk scores...
[7] Assigning risk bands...
[8] Generating explanations...
[9] Generating charts...
[10] Generating report...
[11] Exporting datasets...
[12] Saving models...

PIPELINE COMPLETED SUCCESSFULLY
```

---

## Generated Outputs

Each execution creates a timestamped output folder:

```text
outputs/run_YYYY-MM-DD_HH-MM-SS/
```

### Charts

```text
roc_curve.png
confusion_matrix.png
feature_importance.png
shap_beeswarm.png
risk_distribution.png
```

---

### Reports

```text
executive_summary.txt
taxpayer_scores.csv
high_risk_taxpayers.csv
```

---

### Models

```text
risk_model.pkl
scaler.pkl
```

---

### Metadata

```json
{
    "best_model": "Random Forest",
    "auc_score": 0.96,
    "n_samples": 2000,
    "n_features": 10
}
```

---

## Technologies Used

### Programming

* Python 3.x

### Data Processing

* NumPy
* Pandas

### Machine Learning

* Scikit-learn

### Explainability

* SHAP

### Visualisation

* Matplotlib

### Model Persistence

* Joblib

---

## Potential Enhancements

Future improvements could include:

* Gradient Boosting models (XGBoost, LightGBM)
* Hyperparameter optimisation
* Streamlit dashboard deployment
* API integration using FastAPI
* Real tax authority datasets
* Database connectivity
* Automated testing and CI/CD pipelines
* Docker containerisation

---

## Disclaimer

This project uses **synthetically generated data** for educational and portfolio purposes only.

It does not represent actual taxpayers, tax authority methodologies, or operational compliance frameworks.

---

## Author

**Utuedor Binah**

ACCA | MSc Financial Technology | Executive MBA

Interests:

* Data Engineering
* Data Science
* Machine Learning
* Risk Modelling
* Explainable AI

---

## License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this work with appropriate attribution.
