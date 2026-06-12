# Data Dictionary

## Overview

This document defines the datasets, variables, and derived features used within the Tax Risk Scoring Project.

The project uses synthetically generated taxpayer data to simulate a tax authority compliance risk assessment process.

---

## Dataset Summary

| Attribute          | Description                              |
| ------------------ | ---------------------------------------- |
| Dataset Name       | Taxpayer Risk Dataset                    |
| Source             | Synthetic Data Generation Module         |
| Record Granularity | One record per taxpayer                  |
| File Type          | CSV                                      |
| Raw Dataset        | `data/raw/taxpayers_raw.csv`             |
| Processed Dataset  | `data/processed/taxpayers_processed.csv` |
| Typical Volume     | 2,000 taxpayers                          |
| Primary Use        | Tax compliance risk modelling            |

---

# Raw Variables

## declared_income

| Property          | Description                            |
| ----------------- | -------------------------------------- |
| Definition        | Annual income declared by the taxpayer |
| Data Type         | Float                                  |
| Unit              | Monetary amount                        |
| Generation Method | Log-normal distribution                |
| Example           | 72,541.63                              |
| Modelling Role    | Predictor                              |

---

## expense_ratio

| Property          | Description                          |
| ----------------- | ------------------------------------ |
| Definition        | Ratio of expenses to declared income |
| Data Type         | Float                                |
| Range             | 0.01–0.90                            |
| Generation Method | Beta distribution                    |
| Example           | 0.42                                 |
| Modelling Role    | Predictor                            |

---

## years_trading

| Property          | Description                               |
| ----------------- | ----------------------------------------- |
| Definition        | Number of years the taxpayer has operated |
| Data Type         | Integer                                   |
| Range             | 1–29 years                                |
| Generation Method | Random integer                            |
| Example           | 12                                        |
| Modelling Role    | Predictor                                 |

---

## num_amendments

| Property          | Description                   |
| ----------------- | ----------------------------- |
| Definition        | Number of amended tax filings |
| Data Type         | Integer                       |
| Generation Method | Poisson distribution          |
| Example           | 2                             |
| Modelling Role    | Predictor                     |

---

## offshore_flag

| Property       | Description                                 |
| -------------- | ------------------------------------------- |
| Definition     | Indicates presence of offshore arrangements |
| Data Type      | Binary Integer                              |
| Values         | 0 = No, 1 = Yes                             |
| Example        | 1                                           |
| Modelling Role | Predictor                                   |

---

## late_filings

| Property          | Description                    |
| ----------------- | ------------------------------ |
| Definition        | Number of late tax submissions |
| Data Type         | Integer                        |
| Generation Method | Poisson distribution           |
| Example           | 3                              |
| Modelling Role    | Predictor                      |

---

## sector_risk

| Property       | Description                   |
| -------------- | ----------------------------- |
| Definition     | Industry risk classification  |
| Data Type      | Integer                       |
| Values         | 0 = Low, 1 = Medium, 2 = High |
| Example        | 2                             |
| Modelling Role | Predictor                     |

---

## non_compliant

| Property       | Description                      |
| -------------- | -------------------------------- |
| Definition     | Simulated compliance outcome     |
| Data Type      | Binary Integer                   |
| Values         | 0 = Compliant, 1 = Non-compliant |
| Example        | 1                                |
| Modelling Role | Target Variable                  |

---

# Engineered Features

## income_per_year

| Property       | Description                                 |
| -------------- | ------------------------------------------- |
| Definition     | Average declared income per year of trading |
| Formula        | declared_income ÷ years_trading             |
| Data Type      | Float                                       |
| Modelling Role | Predictor                                   |

---

## amendments_per_year

| Property       | Description                              |
| -------------- | ---------------------------------------- |
| Definition     | Average amendments made per trading year |
| Formula        | num_amendments ÷ years_trading           |
| Data Type      | Float                                    |
| Modelling Role | Predictor                                |

---

## filing_risk_index

| Property       | Description                          |
| -------------- | ------------------------------------ |
| Definition     | Composite filing behaviour indicator |
| Formula        | late_filings + num_amendments        |
| Data Type      | Integer                              |
| Modelling Role | Predictor                            |

---

# Output Variables

## risk_score

| Property   | Description                            |
| ---------- | -------------------------------------- |
| Definition | Probability of taxpayer non-compliance |
| Data Type  | Float                                  |
| Range      | 0.00–1.00                              |
| Source     | Best-performing ML model               |

---

## risk_band

| Property         | Description            |
| ---------------- | ---------------------- |
| Definition       | Categorised risk level |
| Values           | Low, Medium, High      |
| Assignment Rules | Probability thresholds |

| Band   | Threshold |
| ------ | --------- |
| Low    | 0.00–0.30 |
| Medium | 0.30–0.60 |
| High   | 0.60–1.00 |

---

## risk_reason

| Property   | Description                                  |
| ---------- | -------------------------------------------- |
| Definition | Human-readable explanation for elevated risk |
| Data Type  | String                                       |
| Source     | Rule-based explanation engine                |
| Example    | Offshore Account; High Expense Ratio         |

---

# Data Quality Considerations

* Synthetic data is generated using statistical distributions.
* No personally identifiable information (PII) exists.
* Missing values are not intentionally introduced.
* Variable ranges are constrained to realistic business values.
* The target variable is probabilistically simulated and should not be interpreted as real taxpayer behaviour.

---

# Disclaimer

This dataset is entirely synthetic and intended solely for educational, demonstration, and portfolio purposes.
