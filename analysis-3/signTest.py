import csv
import random
import math
# H0: Median =6.0
# Ha: Median!=6.0



def sign_test(data, sample_size):
    median = 6.0  # assuming median to be 6 in H0
    positives = sum(1 for x in data if x > median)
    negatives = sum(1 for x in data if x < median)
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
            print("Reject null hypothesis (H0). The median is significantly different from 6.0 at alpha = 0.05.")
        else:
            print("Accept null hypothesis (H0). The median is not significantly different from 6.0 at alpha = 0.05.")
    else:
        # Calculate critical value using binomial distribution
        critical_value = 1
        
        if min(positives, negatives) <= critical_value:
            print("Reject null hypothesis (H0). The median is significantly different from 6.0 at alpha = 0.05.")
        else:
            print("Accept null hypothesis (H0). The median is not significantly different from 6.0 at alpha = 0.05.")

csv_file_path = './diabetesdataset.csv'
with open(csv_file_path, 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)
    data = list(csv_reader)
    data1 = [float(row[0]) for row in data]  # Assuming the values are in the first column
    
sample_size = 10
if sample_size > len(data):
    sample_size = len(data)

random_samples = random.sample(data, sample_size)
sampledata1 = [float(row[0]) for row in random_samples]

sign_test(sampledata1, sample_size)
