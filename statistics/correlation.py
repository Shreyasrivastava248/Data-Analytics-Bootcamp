# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------
# Load the dataset
# ---------------------------------------------------
# Reading CSV file from the given path
df = pd.read_csv("D:/DATA ANALYTIC/statistics/bank_detail.csv")

# ---------------------------------------------------
# Display basic information about the dataset
# ---------------------------------------------------

# Show first 5 rows of the dataset
print(df.head())

# Show dataset information like:
# column names, data types, null values, etc.
print(df.info())

# ---------------------------------------------------
# Correlation Matrix (Optional)
# ---------------------------------------------------
# Correlation shows the relationship strength
# between numerical columns (-1 to +1)

# Select only integer type columns and calculate correlation
data_corr = df.select_dtypes("int64").corr()

# Create heatmap for correlation matrix
sns.heatmap(data_corr, annot=True, cmap="coolwarm")

# Add title
plt.title("Correlation Heatmap")

# Show graph
plt.show()

# ---------------------------------------------------
# Covariance Matrix
# ---------------------------------------------------
# Covariance shows how two variables vary together.
# Positive value  -> both increase/decrease together
# Negative value  -> one increases while other decreases

# Select only integer type columns
# and calculate covariance matrix
data_cov = df.select_dtypes("int64").cov()

# ---------------------------------------------------
# Plot Heatmap of Covariance Matrix
# ---------------------------------------------------

# Set figure size for better visibility
plt.figure(figsize=(10, 6))

# Create heatmap
sns.heatmap(
    data_cov,
    annot=True,        # Show values inside boxes
    fmt=".2f",         # Display values up to 2 decimal places
    cmap="YlGnBu"      # Color style
)

# Add title to the graph
plt.title("Covariance Heatmap")

# Adjust layout for proper spacing
plt.tight_layout()

# Display the heatmap
plt.show()