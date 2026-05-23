# ---------------------------------------------------
# Import Required Libraries
# ---------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------
# Read CSV file from the given path
df = pd.read_csv("D:/DATA ANALYTIC/statistics/bank_detail.csv")

# ---------------------------------------------------
# Basic Information About Dataset
# ---------------------------------------------------

# Display first 5 rows
print(df.head())

# Display total rows and columns
print(df.shape)

# Display statistical summary
print(df.describe())

# ===================================================
# POSITIVE SKEWNESS
# ===================================================
# Positive skewness means:
# Tail is longer on the RIGHT side
# Mean > Median

# Calculate skewness of age column
print(df["age"].skew())

# Print mean, median and mode
print(
    "Mean   :", df["age"].mean(),
    "\nMedian :", df["age"].median(),
    "\nMode   :", df["age"].mode()[0]
)

# Plot histogram
sns.histplot(x="age", data=df, kde=True)

# Add title
plt.title("Positive Skewness - Age Data")

# Show graph
plt.show()

# ===================================================
# NEGATIVE SKEWNESS
# ===================================================
# Negative skewness means:
# Tail is longer on the LEFT side
# Mean < Median

# Generate random normal data
data = np.random.normal(0, 50, 50)

# Print generated data
print(data)

# Convert into DataFrame
dd = pd.DataFrame({"x": data})

# Print skewness
print(dd["x"].skew())

# Print mean, median and mode
print(
    "Mean   :", dd["x"].mean(),
    "\nMedian :", dd["x"].median(),
    "\nMode   :", dd["x"].mode()[0]
)

# Plot histogram
sns.histplot(x='x', data=dd, kde=True)

# Add title
plt.title("Negative Skewness")

# Show graph
plt.show()

# ===================================================
# NORMAL SKEWNESS / SYMMETRICAL DISTRIBUTION
# ===================================================
# Normal distribution means:
# Mean ≈ Median ≈ Mode
# Skewness value is close to 0

# Create symmetrical data
data = [
    2,3,3,4,4,4,5,5,5,5,
    6,6,6,6,6,
    7,7,7,7,7,7,
    8,8,8,8,8,
    9,9,9,9,
    10,10,10,
    11,11,12
]

# Convert data into DataFrame
dd = pd.DataFrame({"x": data})

# Print skewness
print(dd["x"].skew())

# Print mean, median and mode
print(
    "Mean   :", dd["x"].mean(),
    "\nMedian :", dd["x"].median(),
    "\nMode   :", dd["x"].mode()[0]
)

# Plot histogram
sns.histplot(
    x='x',
    data=dd,
    bins=[2,3,4,5,6,7,8,9,10,11,12],
    kde=True
)

# Add title
plt.title("Normal Distribution / Zero Skewness")

# Show graph
plt.show()