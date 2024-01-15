import pandas as pd
import random
import scipy.stats as stats

# Function to calculate rank sums
def rank_sum(sample1, sample2):
    combined = sample1 + sample2
    sorted_combined = sorted(combined)
    ranks = [sorted_combined.index(value) + 1 + combined[:i].count(value) for i, value in enumerate(combined)]
    rank_sum1 = sum(rank for rank, group in zip(ranks, combined) if group in sample1)
    rank_sum2 = sum(rank for rank, group in zip(ranks, combined) if group in sample2)
    return rank_sum1, rank_sum2

print("\nWilcoxon Rank Sum Test\n")
df = pd.read_csv('./diabetesdataset.csv')

# Separate your data into two groups (e.g., group1 and group2)
group1 = df['Glucose(before Lunch)']
group2 = df['Glucose(after Lunch)']

print("Group 1 (Glucose(before Lunch)):")
print(f"H0: Null hypothesis - No significant difference between the groups.")
print(f"Ha: Alternative hypothesis - There is a significant difference between the groups.")

sample_size_group1 = 11  # Choose the sample size for group 1
sample_size_group2 = 12  # Choose the sample size for group 2

print("\tSample size Group 1: " + str(sample_size_group1))
sample_group1 = random.sample(group1.tolist(), sample_size_group1)
print("\tSample size Group 2: " + str(sample_size_group2))
sample_group2 = random.sample(group2.tolist(), sample_size_group2)

# Perform the Wilcoxon Rank Sum Test manually
rank_sum1, rank_sum2 = rank_sum(sample_group1, sample_group2)
n1 = len(sample_group1)
n2 = len(sample_group2)
U1 = rank_sum1 - (n1 * (n1 + 1)) / 2
U2 = rank_sum2 - (n2 * (n2 + 1)) / 2
U = min(U1, U2)

# Calculate z_cal using R, expected R, and standard deviation of R
expected_U = n1 * n2 / 2
std_dev_U = (n1 * n2 * (n1 + n2 + 1)) / 12 ** 0.5
z_cal = (U - expected_U) / std_dev_U

z_tab=1.9600
# Output the results
print("\tSum of the ranks of minimum sample(R):", U)
print("\tz_cal:", abs(z_cal))
print("\tz_tab:",z_tab)

# Interpret the results
alpha = 0.05  # significance level

if abs(z_cal)<=z_tab:
    conclusion = (
        f"Accept the null hypothesis: There is no significant difference between the groups."
        )
else:
    conclusion = (
        f"Reject the null hypothesis: There is a significant difference between the groups."
        )

print(conclusion)
