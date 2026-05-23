# ---------------------------------------------------
# Import Required Libraries
# ---------------------------------------------------
import numpy as np
import scipy.stats as st

# ===================================================
# QUESTION 1 : CHI-SQUARE GOODNESS OF FIT TEST
# ===================================================
# A fair die is rolled 120 times and the following
# frequencies are observed:
#
# Face 1 -> 22
# Face 2 -> 17
# Face 3 -> 20
# Face 4 -> 26
# Face 5 -> 22
# Face 6 -> 13
#
# Test at 5% significance level whether
# the die is fair.
# ===================================================

# ---------------------------------------------------
# Observed Frequencies
# ---------------------------------------------------
ob = np.array([22, 17, 20, 26, 22, 13])

# ---------------------------------------------------
# Expected Frequencies
# ---------------------------------------------------
# If die is fair:
# Total = 120
# Expected frequency for each face = 120 / 6 = 20
# ---------------------------------------------------

ex = np.array([20, 20, 20, 20, 20, 20])

# ---------------------------------------------------
# Step 1: Define Hypotheses
# ---------------------------------------------------
# H0 : Die is fair
# H1 : Die is not fair
# ---------------------------------------------------

# ---------------------------------------------------
# Step 2: Calculate Chi-Square Test Statistic
# ---------------------------------------------------
# Formula:
#
# χ² = Σ (Observed - Expected)² / Expected
# ---------------------------------------------------

chi_cal = np.sum((ob - ex) ** 2 / ex)

print("Calculated Chi-Square Value :", chi_cal)

# ---------------------------------------------------
# Step 3: Find Critical Table Value
# ---------------------------------------------------
# Degrees of Freedom:
# df = n - 1
# df = 6 - 1 = 5
# ---------------------------------------------------

chi_table = st.chi2.ppf(1 - 0.05, 5)

print("Critical Chi-Square Value :", chi_table)

# ---------------------------------------------------
# Step 4: Decision
# ---------------------------------------------------
# If:
# chi_cal > chi_table
# Reject H0
# ---------------------------------------------------

if chi_cal > chi_table:
    print("Reject H0")
    print("The die is NOT fair.")
else:
    print("Accept H0")
    print("The die is fair.")

# ===================================================
# QUESTION 2 : CHI-SQUARE TEST OF INDEPENDENCE
# ===================================================
# A study was conducted to investigate whether
# there is a relationship between gender and
# preferred music genre.
#
# Test whether there is a significant association
# between gender and music preference.
# ===================================================

# ---------------------------------------------------
# Observed Frequency Table
# ---------------------------------------------------

row1 = np.array([40, 45, 25, 10])
row2 = np.array([35, 30, 20, 30])

# Create observed table
obs = np.array([row1, row2])

print("\nObserved Frequency Table:\n")
print(obs)

# ---------------------------------------------------
# Step 1: Calculate Row Totals
# ---------------------------------------------------
row_totals = np.sum(obs, axis=1)

# ---------------------------------------------------
# Step 2: Calculate Column Totals
# ---------------------------------------------------
col_totals = np.sum(obs, axis=0)

# ---------------------------------------------------
# Step 3: Calculate Grand Total
# ---------------------------------------------------
grand_total = np.sum(obs)

# ---------------------------------------------------
# Step 4: Calculate Expected Frequencies
# ---------------------------------------------------
# Formula:
#
# Expected = (Row Total × Column Total) / Grand Total
# ---------------------------------------------------

exp = np.outer(row_totals, col_totals) / grand_total

print("\nExpected Frequency Table:\n")
print(exp)

# ---------------------------------------------------
# Step 5: Calculate Chi-Square Statistic
# ---------------------------------------------------

chi_test = np.sum((obs - exp) ** 2 / exp)

print("\nCalculated Chi-Square Value :", chi_test)

# ---------------------------------------------------
# Step 6: Find Critical Table Value
# ---------------------------------------------------
# Degrees of Freedom:
#
# df = (rows - 1) × (columns - 1)
#
# df = (2 - 1) × (4 - 1)
# df = 3
# ---------------------------------------------------

chi_table = st.chi2.ppf(1 - 0.05, 3)

print("Critical Chi-Square Value :", chi_table)

# ---------------------------------------------------
# Step 7: Decision
# ---------------------------------------------------

if chi_test > chi_table:
    print("Reject H0")
    print("There IS a significant association between gender and music preference.")
else:
    print("Accept H0")
    print("There is NO significant association between gender and music preference.")