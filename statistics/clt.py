# ---------------------------------------------------
# Import Required Libraries
# ---------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# ---------------------------------------------------
# Generate Population Data
# ---------------------------------------------------
# Create 10,000 random integer values between 10 and 100
pop_data = [np.random.randint(10, 100) for i in range(10000)]

# Print mean of population data
print("Population Mean :", np.mean(pop_data))

# Uncomment below lines if you want to inspect the data

# Print complete population data
print(pop_data)

# Print total number of values
print(len(pop_data))

# ---------------------------------------------------
# Convert Population Data into DataFrame
# ---------------------------------------------------
pop_table = pd.DataFrame({"pop_data": pop_data})

# Print DataFrame
print(pop_table)

# ---------------------------------------------------
# Plot Population Distribution (Optional)
# ---------------------------------------------------
# KDE Plot helps visualize the distribution of data

sns.kdeplot(x="pop_data", data=pop_table)
plt.title("Population Data Distribution")
plt.show()

# ---------------------------------------------------
# Sampling Process
# ---------------------------------------------------
# We will take multiple samples from the population
# and calculate their sample means

sample_mean = []

# Outer loop → Number of samples
for no_sample in range(50):

    # Empty list to store one sample
    sample_data = []

    # Inner loop → Sample size
    for data in range(500):

        # Randomly select one value from population
        sample_data.append(np.random.choice(pop_data))

    # Calculate mean of current sample
    mean_value = np.mean(sample_data)

    # Store sample mean
    sample_mean.append(mean_value)

# ---------------------------------------------------
# Print Mean of All Sample Means
# ---------------------------------------------------
print("Mean of Sample Means :", np.mean(sample_mean))

# ---------------------------------------------------
# Convert Sample Means into DataFrame
# ---------------------------------------------------
sample_M = pd.DataFrame({"sample_mean": sample_mean})

# ---------------------------------------------------
# Plot Sampling Distribution (Optional)
# ---------------------------------------------------
sns.kdeplot(x="sample_mean", data=sample_M)

plt.title("Sampling Distribution of Sample Means")

plt.show()