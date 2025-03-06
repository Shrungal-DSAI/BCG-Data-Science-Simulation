🌟 BCG Data Science Simulation 🚀

  

📌 Project Overview

This project is part of the BCG Data Science Simulation and focuses on customer churn prediction using feature engineering and machine learning techniques. The goal is to analyze customer behavior, engineer meaningful features, and develop a predictive model for churn classification.

📊 Dataset Description

The dataset consists of customer information related to electricity consumption, pricing, and contractual details. Key features include:

Feature Type

Description

Date-related

Activation date, end date, renewal date

Consumption

Last month consumption, yearly consumption, forecasted consumption

Pricing

Peak and off-peak energy prices, yearly and six-month price variations

Profitability

Net and gross margins

Customer Activity

Number of active products, sales channels, and origin of sign-ups

🛠️ Feature Engineering

Feature engineering played a crucial role in improving model performance. Key engineered features include:

Customer Tenure: Days between activation and contract end date.

Consumption Trends: Consumption ratio and forecast deviation.

Price Sensitivity Metrics: Peak vs. off-peak price ratio and yearly price variations.

Profitability Metrics: Profitability ratio and power demand per product.

Handling Missing Values:

Numerical: Filled with median values.

Categorical: Replaced with 'Unknown'.

🎯 Model Training & Evaluation

A Random Forest Classifier was trained on the processed dataset. The dataset was split into training (80%) and testing (20%). The model was evaluated using:

Accuracy: 89.97%

Precision: 87.50%

Recall: 4.59%

F1 Score: 8.72%

Classification Report:
               precision    recall  f1-score   support

           0       0.90      1.00      0.95      2617
           1       0.88      0.05      0.09       305

    accuracy                           0.90      2922
   macro avg       0.89      0.52      0.52      2922
weighted avg       0.90      0.90      0.86      2922

📂 Repository Structure

BCG-Data-Science-Simulation/
│── notebooks/
│   ├── BCGfeatureEngineering.ipynb    # Feature engineering & dataset preprocessing
│   ├── Random4BCG.ipynb               # Model training & evaluation
│
│── data/
│   ├── clean_data_after_eda.csv       # Cleaned dataset after exploratory data analysis
│   ├── data_for_predictions.csv       # Dataset prepared for predictions
│   ├── price_data.csv                 # Energy pricing-related data
│   ├── processed_data.csv             # Final processed dataset
│
│── documents/
│   ├── Data Description.pdf           # Dataset attributes description
│   ├── Executive Summary.pdf          # Summary of the modeling approach & results
│
│── README.md                          # Project documentation

🚀 Next Steps

🔹 Fine-tune hyperparameters for better performance.
🔹 Explore additional feature engineering techniques.
🔹 Compare performance with other ML models (e.g., XGBoost, Logistic Regression).
🔹 Deploy the model for real-time predictions.

💻 How to Run the Project

1️⃣ Clone this repository:

 git clone https://github.com/Shrungal-DSAI/BCG-Data-Science-Simulation.git

2️⃣ Navigate to the project directory:

 cd BCG-Data-Science-Simulation

3️⃣ Install dependencies:

 pip install -r requirements.txt

4️⃣ Run the Jupyter notebooks for feature engineering and model training.

👤 Author

Shrungal Kulkarni

This project is part of a data science simulation exercise with BCG. 🌈📊
