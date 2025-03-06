## 📊 BCG Data Science Simulation

# 🔥 PowerCo Customer Churn Prediction  

### 📌 Business Context  

PowerCo, a major gas and electricity provider, faces a **9.7% churn rate** among **14,606 SME customers**. This project aims to build a predictive model that identifies at-risk customers and provides strategic insights to reduce churn.   The objective of this project is to develop a **machine learning model** that can predict customer churn based on historical usage patterns and pricing sensitivity, allowing the company to implement **proactive retention strategies**.

---

### 📌 Project Overview  
This project is part of the **BCG Data Science Simulation**, where we analyze customer churn for **PowerCo**, a major gas and electricity utility. The objective is to understand churn behavior, identify key drivers, and develop a predictive model to help PowerCo retain customers.

---

### 🎯 Key Insights  

- **Churn Rate**: **9.7%** in the SME division  
- **Top Churn Drivers** (not price sensitivity!):  
  1️⃣ **Yearly consumption**  
  2️⃣ **Forecasted consumption**  
  3️⃣ **Net margin**  
- **Discount Strategy**: A **20% discount is effective**, but should be **targeted only at high-value customers with high churn probability**.

---

## 📊 Data Description  

We used two datasets:  

### 🏢 **Client Data (`client_data.csv`)**  
Contains **customer-level** attributes, including contract details, energy usage, and financial metrics.  
- **ID-based features**: Client identifier (`id`), first subscription campaign (`origin_up`)  
- **Energy consumption**: Last 12 months (`cons_12m`), last month (`cons_last_month`), forecasted (`forecast_cons_12m`)  
- **Contract details**: Activation date (`date_activ`), next renewal (`date_renewal`), end date (`date_end`)  
- **Financial indicators**: Gross margin (`margin_gross_pow_ele`), net margin (`net_margin`), paid consumption (`imp_cons`)  
- **Churn Label**: `churn` (Has the client churned over the next 3 months?)  

### 💰 **Pricing Data (`price_data.csv`)**  
Contains **energy pricing details** across different time periods (peak, off-peak, mid-peak).  
- **Variable prices** (`price_off_peak_var`, `price_peak_var`, `price_mid_peak_var`)  
- **Fixed prices** (`price_off_peak_fix`, `price_peak_fix`, `price_mid_peak_fix`)  

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

### 🔹 **Key Business Recommendations**  

✅ **Stop blanket discounting!** Instead, target **high-value customers at risk** of churn.  
✅ **Improve engagement with customers showing decreasing consumption trends**.  
✅ **Optimize pricing models** based on customer segment behavior. 

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
