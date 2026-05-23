# 📊 Statistics with Python

A collection of Python scripts demonstrating core statistical concepts using real-world examples and the `bank_detail.csv` dataset.

---

## 📁 Project Structure
statistics/
├── bank_detail.csv        # Dataset used across multiple scripts
├── mean.py                # Central tendency (mean, median, mode)
├── variability.py         # Spread measures (range, variance, std, percentile)
├── shape.py               # Skewness and distribution shape
├── correlation.py         # Correlation and covariance heatmaps
├── clt.py                 # Central Limit Theorem simulation
├── z-test.py              # Z-Test hypothesis testing
├── t-test.py              # T-Test (one-sample, two-sample, paired)
├── chi-square-test.py     # Chi-Square (goodness of fit & independence)
└── README.md
---

## 📦 Requirements

Install the required libraries using pip:

```bash
pip install numpy pandas matplotlib seaborn scipy
```

---

## 📌 Script Overview

### 1. `mean.py` — Measures of Central Tendency
- Manual mean calculation using NumPy
- Computes **mean**, **median**, and **mode** on the `age` column
- Plots a histogram with mean, median, and mode lines

---

### 2. `variability.py` — Measures of Variability
- Calculates **range**, **MAD**, **standard deviation**, **variance**
- Computes **percentiles** (Q1, Q3)
- Visualizes with scatter plots and box plots

---

### 3. `shape.py` — Distribution Shape & Skewness
- Demonstrates **positive**, **negative**, and **zero skewness**
- Uses KDE histograms to visualize each type
- Compares mean, median, and mode for each case

---

### 4. `correlation.py` — Correlation & Covariance
- Generates a **correlation heatmap** (`coolwarm` palette)
- Generates a **covariance heatmap** (`YlGnBu` palette)
- Works on all integer columns from `bank_detail.csv`

---

### 5. `clt.py` — Central Limit Theorem
- Simulates a population of 10,000 random values
- Takes **50 samples** of size **500** each
- Plots population distribution vs. sampling distribution of means
- Demonstrates that sample means follow a normal distribution

---

### 6. `z-test.py` — Z-Test Hypothesis Testing
**Question 1:** Tests if students' mean score > 82 (right-tailed)  
**Question 2:** Tests if a new website design increases average purchase amount  
- Uses `scipy.stats.norm.ppf` for critical value
- Right-tailed test with α = 0.05

---

### 7. `t-test.py` — T-Test Hypothesis Testing
**Question 1:** One-sample one-tailed t-test — chip bag weight claim  
**Question 2:** Independent two-sample t-test — team productivity  
**Question 3:** Paired t-test — typing speed before vs. after training  
- Uses `scipy.stats.t.ppf` for critical values
- Both one-tailed and two-tailed tests covered

---

### 8. `chi-square-test.py` — Chi-Square Test
**Question 1:** Goodness of Fit — tests if a die is fair (120 rolls)  
**Question 2:** Test of Independence — gender vs. music preference  
- Uses `scipy.stats.chi2.ppf` for critical values
- Calculates expected frequencies manually

---

## 🗃️ Dataset

**`bank_detail.csv`** — Contains bank customer data with columns including `age`, `job`, and other numeric features used for statistical analysis.

> ⚠️ Update the file path in each script before running:
> ```python
> df = pd.read_csv("your/path/to/bank_detail.csv")
> ```

---

## ▶️ How to Run

```bash
python mean.py
python variability.py
python shape.py
python correlation.py
python clt.py
python z-test.py
python t-test.py
python chi-square-test.py
```

---

## 👤 Author

> Created as part of a Data Analytics learning series covering practical statistics with Python. 