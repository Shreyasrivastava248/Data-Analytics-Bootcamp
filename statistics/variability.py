import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Loading dataset
df = pd.read_csv("D:/DATA ANALYTIC/statistics/bank_detail.csv")

# ==========================================================
# Range
# ==========================================================

# Maximum value
rmax=df['age'].max()
print(rmax)

# Minimum value
rmin=df['age'].min()
print(rmin)

# Range Formula = Maximum - Minimum
ranges=rmax-rmin
print(ranges)

# ==========================================================
# Mean Absolute Deviation (MAD)
# ==========================================================

sec_a=np.array([75,73,68,72,76,65])
sec_b=np.array([70,47,43,96,93,51])

no=np.array([1,2,3,4,5,6])

# Mean of section B
mean=np.mean(sec_b)

# MAD of section A
mad_a=np.sum(np.abs(sec_a-mean))/len(sec_a)
print(mad_a)

# MAD of section B
mad_b=np.sum(np.abs(sec_b-mean))/len(sec_b)
print(mad_b)

# ==========================================================
# Standard Deviation
# ==========================================================

print(np.std(sec_a),np.std(sec_b))

# ==========================================================
# Variance
# ==========================================================

print(np.var(sec_a),np.var(sec_b))

# ==========================================================
# Scatter Plot
# ==========================================================

plt.scatter(sec_a,no,label='sec_a')

plt.figure(figsize=(10,3))

plt.scatter(sec_b,no,color='red',label='sec_b')

# Mean reference line
plt.plot([70,70,70,70,70,70],no,c='green',label="mean")

plt.legend()
plt.show()

# ==========================================================
# Variance of Age Column
# ==========================================================

print(df['age'].var())

# ==========================================================
# Histogram Plot
# ==========================================================

sns.histplot(x='age',data=df)
plt.show()

# ==========================================================
# Dataset Information
# ==========================================================

print(df.describe())

print(df['age'])

# ==========================================================
# Percentile
# ==========================================================

print(
    np.percentile(df['age'], 25),
    (np.percentile(df['age'],75))
)

# ==========================================================
# Box Plot
# ==========================================================

sns.boxplot(x='age',data=df)

plt.show()