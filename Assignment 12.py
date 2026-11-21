import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the customer data
data = pd.read_csv("customer_churn.csv")

# Show missing values
print("Missing values:")
print(data.isnull().sum())

# Fill missing numbers with the column average
data = data.fillna(data.mean(numeric_only=True))

# Basic summary statistics
print("\nSummary:")
print(data.describe())

# Show how many customers churned
print("\nChurn counts:")
print(data["Churn"].value_counts())

# Plot churn counts
data["Churn"].value_counts().plot(kind="bar")
plt.title("Customer Churn")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.show()