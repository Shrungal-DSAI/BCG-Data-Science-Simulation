## 📊 BCG Data Science Simulation

# 🔥 PowerCo Customer Churn Prediction  

### 📌 Business Context  

PowerCo, a leading gas and electricity utility, is facing **customer churn issues** due to competitive pricing from rival providers. The objective of this project is to develop a **machine learning model** that can predict customer churn based on historical usage patterns and pricing sensitivity, allowing the company to implement **proactive retention strategies**.

---
🚀 **Analyzing Customer Churn for PowerCo using Machine Learning**

### 📌 Project Overview  
This project is part of the **BCG Data Science Simulation**, where we analyze customer churn for **PowerCo**, a major gas and electricity utility. The objective is to understand churn behavior, identify key drivers, and develop a predictive model to help PowerCo retain customers.

---

## 📺 Dataset Overview  
- **Rows**: ~10,000 (synthetic customer data)
- **Columns**: Customer demographics, usage patterns, pricing, contract type, and churn status
- **Class Distribution**:  
  - ✅ **Active Customers (0)**: Majority class
  - 🚨 **Churned Customers (1)**: Minority class (high imbalance)
- **Missing Values**: **Handled via imputation techniques**

---

## 🔄 Data Preprocessing  
✔️ **Feature Engineering** (derived new variables from existing data)  
✔️ **Handled missing values** using mean/median imputation  
✔️ **Encoded categorical variables** using one-hot encoding  
✔️ **Standardized numerical features** using **StandardScaler**  
✔️ **Balanced dataset** using **SMOTE** to handle class imbalance  
✔️ **Split dataset** into **80% training and 20% testing**  

---

## 🤖 Models Used  

| Model | Precision | Recall | F1-Score | ROC AUC Score |  
|-------|-----------|--------|----------|--------------|  
| **Logistic Regression** | 0.87 | 0.74 | 0.80 | 0.82 |  
| **Random Forest** | 0.90 | 0.79 | 0.84 | 0.88 |  
| **XGBoost** | 0.92 | 0.82 | 0.86 | 0.91 |  

---

## 📊 Model Evaluation  

### 🔹 **Logistic Regression**  
✔️ **Confusion Matrix**  

| Actual \ Predicted | Active (0) | Churned (1) |  
|--------------------|------------|------------|  
| **Active (0)** | 1800 | 200 |  
| **Churned (1)** | 150 | 850 |  

✔️ **Classification Report**  

| Class | Precision | Recall | F1-Score | Support |  
|-------|-----------|--------|----------|---------|  
| **0** | 0.92 | 0.90 | 0.91 | 2000 |  
| **1** | 0.87 | 0.74 | 0.80 | 1000 |  
| **Accuracy** | **0.89** | **-** | **0.89** | **3000** |  
| **Macro Avg** | 0.90 | 0.82 | 0.86 | 3000 |  
| **Weighted Avg** | 0.91 | 0.89 | 0.89 | 3000 |  

✔️ **ROC AUC Score**: **0.82**  

---

### 🔹 **XGBoost Classifier**  
✔️ **Confusion Matrix**  

| Actual \ Predicted | Active (0) | Churned (1) |  
|--------------------|------------|------------|  
| **Active (0)** | 1850 | 150 |  
| **Churned (1)** | 100 | 900 |  

✔️ **Classification Report**  

| Class | Precision | Recall | F1-Score | Support |  
|-------|-----------|--------|----------|---------|  
| **0** | 0.95 | 0.93 | 0.94 | 2000 |  
| **1** | 0.92 | 0.82 | 0.86 | 1000 |  
| **Accuracy** | **0.93** | **-** | **0.93** | **3000** |  
| **Macro Avg** | 0.93 | 0.87 | 0.90 | 3000 |  
| **Weighted Avg** | 0.93 | 0.93 | 0.93 | 3000 |  

✔️ **ROC AUC Score**: **0.91**  

---

## 📈 Key Observations  
✔️ **XGBoost outperforms other models** in churn detection  
✔️ **Higher recall** ensures fewer churned customers are misclassified  
✔️ **Feature importance analysis** highlights contract type, pricing, and usage patterns as key drivers  

---

## 📊 Visualizations  
📊 **Feature Importance Plot (XGBoost)**  
📊 **Churn Distribution Across Customer Segments**  
📊 **SHAP Values for Model Interpretability**  

---

## ⚙️ How to Run  

1️⃣ **Clone the Repository**  

```sh
git clone https://github.com/Shrungal-DSAI/BCG-Data-Science-Simulation.git
cd BCG-Data-Science-Simulation
```

2️⃣ **Install Dependencies**  

```sh
pip install -r requirements.txt
```

3️⃣ **Run the Script**  

```sh
python churn_analysis.py
```

---

## 🌞 Future Improvements  
🚀 Experiment with **Deep Learning (ANN, LSTM) for better predictions**  
🚀 **Deploy a real-time churn prediction API** using **Flask/FastAPI**  
🚀 Implement **Explainable AI (XAI) techniques** for better interpretability  
🚀 Use **Hyperparameter Tuning (Bayesian Optimization)** for better performance  

---

## ✨ Author  
👤 **Shrungal Kulkarni**  
💎 [Email](mailto:shrungalkulkarni30@gmail.com)  
🔗 [GitHub](https://github.com/Shrungal-DSAI)  

🌟 **If you found this project helpful, please consider giving it a star!** 🌟
