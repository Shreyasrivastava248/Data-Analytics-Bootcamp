# ---------------------------------------------------
# Import Required Libraries
# ---------------------------------------------------
import scipy.stats as st
import numpy as np

# ===================================================
# QUESTION 1 : ONE-TAILED T-TEST
# ===================================================
# A manufacturer claims that the average weight
# of a bag of potato chips is 150 grams.
#
# A sample of 25 bags is taken.
#
# Sample Mean = 148 grams
# Sample Standard Deviation = 5 grams
#
# Test the claim using a one-tailed t-test
# at 5% significance level.
# ===================================================

# ---------------------------------------------------
# Given Data
# ---------------------------------------------------
alpha = 0.05
sample_mean = 148
pop_mean = 150
sample_std = 5
n = 25

# Degrees of Freedom
df = n - 1

# ---------------------------------------------------
# Step 1: Define Hypotheses
# ---------------------------------------------------
# H0 : μ = 150
# H1 : μ < 150
#
# This is a LEFT-TAILED TEST
# ---------------------------------------------------

# ---------------------------------------------------
# Step 2: Find Critical T Value
# ---------------------------------------------------
t_table = st.t.ppf(alpha, df)

print("Critical T Value :", t_table)

# ---------------------------------------------------
# Step 3: Calculate T-Test Statistic
# ---------------------------------------------------
# Formula:
#
#            x̄ - μ
# t = -------------------
#        s / √n
# ---------------------------------------------------

t_cal = (sample_mean - pop_mean) / (sample_std / np.sqrt(n))

print("Calculated T Value :", t_cal)

# ---------------------------------------------------
# Step 4: Decision
# ---------------------------------------------------
if t_cal < t_table:
    print("Reject H0")
    print("Manufacturer's claim is NOT correct.")
else:
    print("Accept H0")
    print("Manufacturer's claim is correct.")

# ===================================================
# QUESTION 2 : INDEPENDENT TWO-SAMPLE T-TEST
# ===================================================
# A company wants to test whether there is
# a difference in productivity between two teams.
#
# Team A Mean = 80
# Team B Mean = 75
#
# Standard Deviations:
# Team A = 5
# Team B = 6
#
# Sample Size = 20 each
#
# Test at 5% significance level.
# ===================================================

# ---------------------------------------------------
# Given Data
# ---------------------------------------------------
xa = 80
xb = 75

sa = 5
sb = 6

n = 20

alpha = 0.05

# Degrees of Freedom
df = (n + n) - 2

# ---------------------------------------------------
# Step 1: Define Hypotheses
# ---------------------------------------------------
# H0 : No difference between teams
# H1 : Difference exists between teams
#
# This is a TWO-TAILED TEST
# ---------------------------------------------------

# ---------------------------------------------------
# Step 2: Find Critical T Value
# ---------------------------------------------------
# For two-tailed test:
# alpha/2 is used
# ---------------------------------------------------

t_table = st.t.ppf(1 - alpha/2, df)

print("\nCritical T Value :", t_table)

# ---------------------------------------------------
# Step 3: Calculate T-Test Statistic
# ---------------------------------------------------

t_cal = (xa - xb) / np.sqrt((sa**2 / n) + (sb**2 / n))

print("Calculated T Value :", t_cal)

# ---------------------------------------------------
# Step 4: Decision
# ---------------------------------------------------
if abs(t_cal) > t_table:
    print("Reject H0")
    print("There IS a significant difference between teams.")
else:
    print("Accept H0")
    print("There is NO significant difference between teams.")

# ===================================================
# QUESTION 3 : PAIRED T-TEST
# ===================================================
# A company wants to check whether a new
# training program improves typing speed.
#
# Typing speed recorded:
# - Before training
# - After training
#
# Test at 5% significance level.
# ===================================================

# ---------------------------------------------------
# Given Data
# ---------------------------------------------------

After = np.array([
    60, 70, 55, 75, 65, 80, 50, 85, 90, 70,
    75, 65, 55, 60, 50, 80, 65, 55, 70, 75
])

Before = np.array([
    50, 60, 45, 65, 55, 70, 40, 75, 80, 65,
    70, 60, 50, 55, 45, 75, 60, 50, 65, 70
])

alpha = 0.05

# Number of observations
n = len(After)

# Degrees of Freedom
df = n - 1

# ---------------------------------------------------
# Step 1: Calculate Difference
# ---------------------------------------------------
diff = After - Before

# ---------------------------------------------------
# Step 2: Calculate Mean and Standard Deviation
# ---------------------------------------------------
mean_diff = np.mean(diff)

std_diff = np.std(diff, ddof=1)

# ---------------------------------------------------
# Step 3: Find Critical T Value
# ---------------------------------------------------
t_table = st.t.ppf(1 - alpha/2, df)

print("\nCritical T Value :", t_table)

# ---------------------------------------------------
# Step 4: Calculate Paired T-Test Statistic
# ---------------------------------------------------
# Formula:
#
#              d̄
# t = -------------------
#        sd / √n
# ---------------------------------------------------

t_cal = mean_diff / (std_diff / np.sqrt(n))

print("Calculated T Value :", t_cal)

# ---------------------------------------------------
# Step 5: Decision
# ---------------------------------------------------
if abs(t_cal) > t_table:
    print("Reject H0")
    print("Training program IMPROVES typing speed.")
else:
    print("Accept H0")
    print("Training program does NOT improve typing speed.")