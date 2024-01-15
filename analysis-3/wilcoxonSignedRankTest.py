import pandas as pd
import random
import numpy as np
import scipy.stats as stats
def wilcoxon_signed_rank_test(sample_before, sample_after):
    # Calculate the differences between paired observations
    differences = [a - b for a, b in zip(sample_before, sample_after)]

    # Remove pairs where the difference is zero
    differences = [diff for diff in differences if diff != 0]

    # Calculate absolute differences and ranks
    abs_diff = np.abs(differences)
    ranks = [abs(rank) for rank in stats.rankdata(abs_diff)]

    # Assign ranks to the differences considering their signs
    signed_ranks = [rank if diff > 0 else -rank for rank, diff in zip(ranks, differences)]

    # Calculate the sum of positive ranks and negative ranks
    sum_positive_ranks = sum(rank for rank in signed_ranks if rank > 0)
    sum_negative_ranks = sum(rank for rank in signed_ranks if rank < 0)

    # Calculate the test statistic (T)
    T = min(sum_positive_ranks, abs(sum_negative_ranks))

    # Calculate the number of pairs
    n = len(differences)

    # Calculate the expected value and standard deviation of T
    expected_T = n * (n + 1) / 4
    std_dev_T = (n * (n + 1) * (2 * n + 1) / 24) ** 0.5

    # Calculate the Z-score
    z = abs(T - expected_T) / std_dev_T

    
    

    return z,T

print("\nWilcoxon Signed-Rank Test\n")

df = pd.read_csv('./diabetesdataset.csv')

print("Paired Data (Glucose(before Lunch) and Glucose(after Lunch)):")
print(f"H0: Null hypothesis - No significant difference between the two paired samples.")
print(f"Ha: Alternative hypothesis - There is a significant difference between the two paired samples.")

sample_size = 25  # Choose the sample size (n < 30)

print("\tSample size: " + str(sample_size))

# Sample the data for 'Glucose(before Lunch)' and 'Glucose(after Lunch)' columns
sample_before = random.sample(df['Glucose(before Lunch)'].tolist(), sample_size)
sample_after = random.sample(df['Glucose(after Lunch)'].tolist(), sample_size)

# Perform the Wilcoxon Signed-Rank Test manually
z_cal,statistic = wilcoxon_signed_rank_test(sample_before, sample_after)
z_tab=1.9600
# Output the results
print("\tWilcoxon Signed-Rank Test statistic:", statistic)
print("\tz_cal:", abs(z_cal))
print("\tz_tab:",z_tab)

# Interpret the results
alpha = 0.05  # significance level
if abs(z_cal) <= z_tab:
    conclusion = (
       f"Accept the null hypothesis: There is no significant difference between the paired samples."
        )
else:
    conclusion = (
        f"Reject the null hypothesis: There is a significant difference between the paired samples."
        )

print(conclusion)
