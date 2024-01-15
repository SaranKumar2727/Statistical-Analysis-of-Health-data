import csv
import random
import math
import pandas as pd



def sign_test(data, sample_size):
    
    positives = sum(1 for x in data if x > 0)
    negatives = sum(1 for x in data if x < 0)

    zeroes = sample_size - (positives + negatives)
    
    n = sample_size - zeroes
    print("No. of zeroes:", zeroes)
    print("No. of positive signs:", positives)
    print("No. of negative signs:", negatives)
    print("Critical n value (sample_size - no. of zeroes):", n)
    
    if sample_size > 26:
        z_cal = abs(min(positives, negatives)+0.05 - (n / 2)) / math.sqrt(sample_size / 2)
        critical_value = 1.9600  # Critical value at alpha = 0.05 for a two-tailed test
        
        print("z_calculated:", z_cal)
        if z_cal > critical_value:
            print("Reject null hypothesis (H0). Glucose levels will increase(claim)")
        else:
            print("Accept null hypothesis (H0). Glucose levels will not increase.")
    else:
        # Calculate critical value using binomial distribution
        critical_value = int(input("enter the crical value: "))
        
        if min(positives, negatives) <= critical_value:
            print("Reject null hypothesis (H0). Glucose levels will increase(claim) ")
        else:
            print("Accept null hypothesis (H0). Glucose levels will not increase")

file_path = './diabetesdataset.csv'
data = pd.read_csv(file_path)
sample_before = data['Glucose(before Lunch)']
sample_after = data['Glucose(after Lunch)']

related_data = list(zip(sample_before, sample_after))

sample_size = 8

random_samples = random.sample(related_data, sample_size)

print("Random samples:",random_samples)

# Calculate the differences
differences = [after - before for before, after in random_samples]

sign_test(differences, sample_size)
