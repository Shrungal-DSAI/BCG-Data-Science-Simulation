## 📊 BCG Data Science Simulation

# 🔥 PowerCo Customer Churn Prediction  

### 📌 Business Context  

PowerCo, a leading gas and electricity utility, is facing **customer churn issues** due to competitive pricing from rival providers. The objective of this project is to develop a **machine learning model** that can predict customer churn based on historical usage patterns and pricing sensitivity, allowing the company to implement **proactive retention strategies**.

---

### 📌 Project Overview  
This project is part of the **BCG Data Science Simulation**, where we analyze customer churn for **PowerCo**, a major gas and electricity utility. The objective is to understand churn behavior, identify key drivers, and develop a predictive model to help PowerCo retain customers.

---

## 📺 Dataset Overview  
- 📁 **Dataset:** Proprietary PowerCo dataset  
- 📊 **Rows:** 10,000+ customers  
- 🔢 **Features:** Usage patterns, contract type, monthly charges, and customer service interactions  
- 🎯 **Target Variable:** **Churn (1: Yes, 0: No)** 
- **Class Distribution**:  
  - ✅ **Active Customers (0)**: Majority class
  - 🚨 **Churned Customers (1)**: Minority class (high imbalance)
- **Missing Values**: **Handled via imputation techniques**

---

## 🛠️ Methodology  

This project follows a structured **data science approach**:  

1️⃣ **Exploratory Data Analysis (EDA)**  
   - Identified patterns in churn behavior  
   - Analyzed feature correlations and importance  

2️⃣ **Data Preprocessing**  
   - **Handled missing values** and categorical encoding  
   - **Standardized numerical features**  
   - **Feature selection** to improve model performance  

3️⃣ **Model Training & Evaluation**  
   - Used **Logistic Regression, Random Forest, and XGBoost**  
   - Applied **Grid Search** for hyperparameter tuning  
   - Evaluated performance with **ROC-AUC, Precision-Recall curves**  

---

## 🤖 Models Used  

| Model | Precision | Recall | F1-Score | ROC AUC Score |  
|-------|-----------|--------|----------|--------------|  
| **Logistic Regression** | 0.87 | 0.74 | 0.80 | 0.82 |  
| **Random Forest** | 0.90 | 0.79 | 0.84 | 0.88 |  
| **XGBoost** | 0.92 | 0.82 | 0.86 | 0.91 |  

✔️ **XGBoost** achieved the best balance of precision and recall, making it the top-performing model. 

---

## 📈 Key Observations  
✔️ **XGBoost outperforms other models** in churn detection  
✔️ **Higher recall** ensures fewer churned customers are misclassified  
✔️ **Feature importance analysis** highlights contract type, pricing, and usage patterns as key drivers  

🔹 **Pricing Sensitivity**: Customers on flexible contracts were **2.5x more likely** to churn.  
🔹 **Usage Pattern Influence**: Higher energy users showed **lower churn rates**, likely due to discounts.  
🔹 **Customer Service Impact**: Poor service ratings were a **major churn predictor**.  

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
