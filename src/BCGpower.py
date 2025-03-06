import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Step 1: Check the current working directory and load the dataset
print("Current Working Directory:", os.getcwd())

# Try to load the client data CSV file with error handling
try:
    client_data = pd.read_csv('C:/Users/Admin/Downloads/client_data.csv')  # Update with correct path
    print("Client data loaded successfully!")
except FileNotFoundError as e:
    print("Error: 'client_data.csv' not found. Please check the file path.")
    exit()

# Step 2: Review the data structure (columns, data types, etc.)
print("Data Types of Columns:\n", client_data.dtypes)

# Step 3: Descriptive statistics to understand the data
print("\nDescriptive Statistics:\n", client_data.describe())

# Step 4: Checking for missing values in the dataset
print("\nMissing Values in Each Column:\n", client_data.isnull().sum())

# Step 5: Exploratory Data Analysis (EDA)
# Visualizing the distributions of numerical columns
numerical_columns = client_data.select_dtypes(include=[np.number]).columns.tolist()

for column in numerical_columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(client_data[column], kde=True)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

# Step 6: Correlation Heatmap
# Visualizing the correlation between numerical columns
correlation_matrix = client_data[numerical_columns].corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', cbar=True)
plt.title('Correlation Matrix')
plt.show()

# Step 7: Feature Engineering - Check for potential useful transformations
# Add any feature engineering ideas here if needed, such as creating new features or transforming existing ones.

# Example: Create a new column based on existing data, e.g., age of the client based on contract dates.
client_data['date_activ'] = pd.to_datetime(client_data['date_activ'], errors='coerce')
client_data['date_end'] = pd.to_datetime(client_data['date_end'], errors='coerce')
client_data['contract_duration'] = (client_data['date_end'] - client_data['date_activ']).dt.days / 365

# Step 8: Investigate churn (target variable) based on features
# Visualizing the distribution of churned vs non-churned clients
plt.figure(figsize=(8, 6))
sns.countplot(x='churn', data=client_data)
plt.title('Churn Distribution')
plt.xlabel('Churn (0 = No, 1 = Yes)')
plt.ylabel('Count')
plt.show()

# Explore relationships between churn and other variables, e.g., customer activity and consumption
plt.figure(figsize=(10, 6))
sns.boxplot(x='churn', y='cons_12m', data=client_data)
plt.title('Electricity Consumption vs Churn')
plt.xlabel('Churn')
plt.ylabel('Electricity Consumption (12 months)')
plt.show()

# Step 9: Review key insights from the EDA
# Based on the visualizations and descriptive statistics, consider:
# - Which features have the most influence on churn?
# - Any correlations between features (e.g., consumption vs. price)?
# - Outliers or missing data handling strategies?

# Optional: Save the cleaned data or insights to a new file
client_data.to_csv('cleaned_client_data.csv', index=False)

# Optional: Save visualizations
# Example: Save the correlation heatmap
correlation_matrix_fig = plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', cbar=True)
correlation_matrix_fig.savefig('correlation_heatmap.png')

print("EDA and analysis completed. Visualizations and data saved.")
