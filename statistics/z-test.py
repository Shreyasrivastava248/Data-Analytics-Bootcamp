import scipy.stats as st
import numpy as np

# ---------------------------------------------------
# Question:
# ---------------------------------------------------
# A teacher claims that the mean score of students
# in his class is greater than 82 with a standard
# deviation of 20.
#
# A sample of 81 students was selected and the
# sample mean score was 90.
#
# Test whether the teacher's claim is correct
# using Hypothesis Testing.
# ---------------------------------------------------

# Import Required Libraries
import numpy as np
import scipy.stats as st

# ---------------------------------------------------
# Given Data
# ---------------------------------------------------

# Sample Mean
sam_x = 90

# Population Mean (Claimed Mean)
p_u = 82

# Population Standard Deviation
p_std = 20

# Sample Size
n = 81

# Significance Level
ap = 0.05

# ---------------------------------------------------
# Step 1: Define Hypotheses
# ---------------------------------------------------
# H0 (Null Hypothesis):
# Mean score <= 82
#
# H1 (Alternative Hypothesis):
# Mean score > 82
#
# Since the claim is "greater than",
# this is a RIGHT-TAILED TEST.
# ---------------------------------------------------

# ---------------------------------------------------
# Step 2: Calculate Z-Test Value
# ---------------------------------------------------
# Formula:
#
#           x̄ - μ
# Z = ----------------
#       σ / √n
# ---------------------------------------------------

z_cal = (sam_x - p_u) / (p_std / np.sqrt(n))

# Print calculated Z value
print("Calculated Z Value :", z_cal)

# ---------------------------------------------------
# Step 3: Find Critical Z Value
# ---------------------------------------------------
# For right-tailed test:
# Zα = norm.ppf(1 - alpha)
# ---------------------------------------------------

z_table = st.norm.ppf(1 - ap)

# Print table value
print("Critical Z Value :", z_table)

# ---------------------------------------------------
# Step 4: Decision Rule
# ---------------------------------------------------
# If:
# Z_cal > Z_table
# Reject H0
#
# Otherwise:
# Accept H0
# ---------------------------------------------------

if z_cal > z_table:
    print("Reject H0")
    print("Teacher's claim is CORRECT.")
else:
    print("Accept H0")
    print("Teacher's claim is NOT correct.")

# # ---------------------------------------------------
# Import Required Libraries
# ---------------------------------------------------
import numpy as np
import scipy.stats as st

# ===================================================
# QUESTION 2
# ===================================================
# Scenario:
#
# An e-commerce company wants to check whether
# a new website design increases the average
# customer purchase amount.
#
# We compare:
# - Old Website Design
# - New Website Design
#
# Goal:
# Check whether the new design performs better.
# ===================================================

# ---------------------------------------------------
# Old Website Design Data
# ---------------------------------------------------
old_design_data = np.array([
    45.2, 42.8, 38.9, 43.5, 41.0, 44.6, 40.5, 42.7, 39.8,
    41.4, 44.3, 39.7, 42.1, 40.6, 43.0, 42.2, 41.5, 39.6,
    44.0, 43.1, 38.7, 43.9, 42.0, 41.9, 42.8, 43.7, 41.3,
    40.9, 42.5, 41.6
])

# ---------------------------------------------------
# New Website Design Data
# ---------------------------------------------------
new_design_data = np.array([
    48.5, 49.1, 50.2, 47.8, 48.7, 49.9, 48.0, 50.5, 49.8,
    49.6, 48.2, 48.9, 49.7, 50.3, 49.4, 50.1, 48.6, 48.3,
    49.0, 50.0, 48.4, 49.3, 49.5, 48.8, 50.6, 50.4, 48.1,
    49.2, 50.7, 50.8
])

# ---------------------------------------------------
# Given Information
# ---------------------------------------------------

# Population Standard Deviation
pop_std = 2.5

# Sample Size
n_sp = len(new_design_data)

# Significance Level
apl = 0.05

# ---------------------------------------------------
# Calculate Means
# ---------------------------------------------------

# Mean of old website purchase amount
mean_of_old = np.mean(old_design_data)

# Mean of new website purchase amount
mean_of_new = np.mean(new_design_data)

# Print means
print("Old Design Mean :", mean_of_old)
print("New Design Mean :", mean_of_new)

# ---------------------------------------------------
# Step 1: Define Hypotheses
# ---------------------------------------------------
# H0 (Null Hypothesis):
# New design is NOT better
#
# H1 (Alternative Hypothesis):
# New design performs better
#
# Since we are checking "greater than",
# this is a RIGHT-TAILED TEST.
# ---------------------------------------------------

# ---------------------------------------------------
# Step 2: Calculate Z-Test Value
# ---------------------------------------------------
# Formula:
#
#          X̄1 - X̄2
# Z = -------------------
#       σ / √n
# ---------------------------------------------------

z_cal = (mean_of_new - mean_of_old) / (pop_std / np.sqrt(n_sp))

# Print calculated Z value
print("Calculated Z Value :", z_cal)

# ---------------------------------------------------
# Step 3: Find Critical Z Value
# ---------------------------------------------------
# For right-tailed test:
# Zα = norm.ppf(1 - alpha)
# ---------------------------------------------------

z_table = st.norm.ppf(1 - apl)

# Print critical Z value
print("Critical Z Value :", z_table)

# ---------------------------------------------------
# Step 4: Decision Making
# ---------------------------------------------------
# If:
# Z_cal > Z_table
# Reject H0
#
# Otherwise:
# Accept H0
# ---------------------------------------------------

if z_cal > z_table:
    print("Reject H0")
    print("New website design performs BETTER.")
else:
    print("Accept H0")
    print("New website design does NOT perform better.")