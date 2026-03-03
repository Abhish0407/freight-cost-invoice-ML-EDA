# 📦 Vendor Invoice Intelligence System

### Freight Cost Prediction & Invoice Risk Flagging

---

## 📌 Table of Contents

* [Project Overview](#project-overview)
* [Business Objectives](#business-objectives)
* [Data Sources](#data-sources)
* [Exploratory Data Analysis](#exploratory-data-analysis-eda)
* [Models Used](#models-used)
* [Evaluation Metrics](#evaluation-metrics)
* [End-to-End Application](#end-to-end-application)
* [Project Structure](#project-structure)
* [How to Run This Project](#how-to-run-this-project)
* [Author & Contact](#author--contact)

---

## 🚀 Project Overview

This project implements an **end-to-end machine learning system** designed to support finance and procurement teams by:

1. **Predicting expected freight cost** for vendor invoices.
2. **Flagging high-risk invoices** that require manual review due to abnormal cost, freight, or operational patterns.

The system covers the complete ML lifecycle:

* Data extraction from SQL database
* Feature engineering & preprocessing
* Model training with hyperparameter tuning
* Model persistence using `joblib`
* Interactive Streamlit dashboard for real-time inference

---

## 🎯 Business Objectives

### 1️⃣ Freight Cost Prediction (Regression)

**Objective:**
Predict the expected freight cost for a vendor invoice using quantity, invoice value, and historical purchasing behavior.

**Why it matters:**

* Freight is a significant component of total landed cost.
* Poor freight estimation impacts margin analysis and budgeting.
* Early prediction improves procurement planning and vendor negotiation.
*
![Freight Cost Prediction App](Screenshots/regression.png)
---

### 2️⃣ Invoice Risk Flagging (Classification)

**Objective:**
Predict whether a vendor invoice should be flagged for manual approval due to abnormal cost, freight, or delivery patterns.

**Why it matters:**

* Manual invoice review does not scale efficiently.
* Financial leakage often occurs in large or complex invoices.
* Early risk detection improves audit efficiency and operational control.
*
![Invoice Risk Flagging App](Screenshots/classification.png)
---

## 🗄 Data Sources

Data is stored in a relational **SQLite database (`inventory.db`)** containing:

* `vendor_invoice` – Invoice-level financial and timing data
* `purchases` – Item-level purchase details
* `purchase_prices` – Reference purchase prices
* `begin_inventory`, `end_inventory` – Inventory snapshots

SQL aggregations are used to generate invoice-level features such as:

* Total item quantity
* Total item dollars
* Average receiving delay
* Days from PO to invoice
* Days to payment

---

## 📊 Exploratory Data Analysis (EDA)

EDA focused on business-driven questions:

* Do flagged invoices have higher financial exposure?
* Does freight scale linearly with quantity?
* Does freight depend on invoice value?
* Are delayed deliveries associated with invoice risk?

Statistical tests (t-tests) were performed to confirm whether flagged invoices differ significantly from normal invoices.

---

## 🤖 Models Used

### 🔹 Regression (Freight Prediction)

* Linear Regression (baseline)
* Decision Tree Regressor
* ✅ Random Forest Regressor (final model)

---

### 🔹 Classification (Invoice Flagging)

* Logistic Regression (baseline)
* Decision Tree Classifier
* ✅ Random Forest Classifier (final model with GridSearchCV)

Hyperparameter tuning is performed using **GridSearchCV** with **F1-score** to handle potential class imbalance.

---

## 📈 Evaluation Metrics

### Freight Prediction

* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)
* R² Score

---

### Invoice Flagging

* Accuracy
* Precision
* Recall
* F1-score
* Classification report
* Feature importance analysis

---

## 🖥 End-to-End Application

A **Streamlit web application** demonstrates the complete ML pipeline:

✔ Input invoice details
✔ Predict expected freight cost
✔ Flag invoices in real time
✔ Provide human-readable approval recommendations

Users can switch between:

* Freight Cost Prediction
* Invoice Manual Approval Flag

---

## 📂 Project Structure

```
Freight_cost_predictor/
│
├── data/
│   └── inventory.db
│
├── invoice_flagging/
│   ├── data_preprocessing.py
│   ├── model_evaluation.py
│   ├── train.py
│
├── inference/
│   ├── predict_freight.py
│   ├── predict_invoice_flag.py
│
├── models/
│   ├── predict_freight_model.pkl
│   ├── predict_flag_invoice.pkl
│   ├── scaler.pkl
│
├── notebooks/
│
├── app.py
│
└── venv/
```

---

## ▶️ How to Run This Project

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd Freight_cost_predictor
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
.\venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install pandas numpy scikit-learn streamlit joblib plotly
```

(Optional) Create a requirements file:

```bash
pip freeze > requirements.txt
```

---

### 4️⃣ Train models (if needed)

```bash
python invoice_flagging/train.py
```

---

### 5️⃣ Run Streamlit app

```bash
streamlit run app.py
```

---

## 👤 Author & Contact

**Abhishek Raj**
PL-300 Certified Data Analyst | Machine Learning & Data Enthusiast

📧 Email: [araj9797@gmail.com](mailto:araj9797@gmail.com)
🔗 LinkedIn: https://www.linkedin.com/in/abhishek-raj1234


---

> This project demonstrates practical implementation of regression and classification models integrated into a production-style ML application.
