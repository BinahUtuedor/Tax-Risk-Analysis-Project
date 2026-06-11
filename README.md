Project Structure
```text
tax_risk_scoring_project/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── outputs/
│   ├── run_YYYY-MM-DD_HH-MM-SS/
│       ├── charts/
│       │     ├── roc_curve.png
│       │     ├── confusion_matrix.png
│       │     ├── shap_beeswarm.png
│       │     ├── feature_importance.png 
│       │     └── risk_distribution.png
│       ├── reports/
│       │     ├── executive_summary.txt
│       │     ├── taxpayer_scores.csv 
│       │     └── high_risk_taxpayers.csv
│       ├── models/
│       │     ├── feature_importance.png 
│       │     └── risk_distribution.png
│       └── metadata.json
│
├── src/
│   ├── __init__.py
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