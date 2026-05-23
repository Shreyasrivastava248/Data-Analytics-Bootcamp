import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading dataset
df = pd.read_csv("D:/DATA ANALYTIC/statistics/bank_detail.csv")

# ==========================================================
# Manual Mean Calculation Using Simple Array
# ==========================================================

ar=np.array([1,3,4,7,5,9])

# Manual formula of mean
print(np.sum(ar)/len(ar))

# Mean using NumPy
print(np.mean(ar))

# ==========================================================
# Checking Dataset
# ==========================================================

print(df.head(5))

# Mean directly from dataframe
print(df['age'].mean())

# ==========================================================
# Measure of Central Tendency
# ==========================================================

# Calculating Mean
mn = (np.mean(df['age']))

# Calculating Median
me = (np.median(df['age']))

# Calculating Mode
mo = df['age'].mode()[0]

print(mn)
print(me)
print(mo)

# Count of job categories
print(df['job'].value_counts())

# ==========================================================
# Histogram Plot
# ==========================================================

sns.histplot(
    x='age',
    data=df,
    bins=[i for i in range(20,91,10)]
)

# ==========================================================
# Plotting Mean Line
# ==========================================================

plt.plot(
    [mn for i in range(0,2000)],
    [i for i in range(0,2000)],
    c='red',
    label='mean'
)

# ==========================================================
# Plotting Median Line
# ==========================================================

plt.plot(
    [me for i in range(0,1800)],
    [i for i in range(0,1800)],
    c='orange',
    label='median'
)

# ==========================================================
# Plotting Mode Line
# ==========================================================

plt.plot(
    [mo for i in range(0,1800)],
    [i for i in range(0,1800)],
    c='green',
    label='mode'
)

# Display legend
plt.legend()

# Display graph
plt.show()