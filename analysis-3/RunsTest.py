import csv
import random



def runs_test(data):
    n = len(data)
    median = sorted(data)[n // 2]
    print("median :",median)
    runs_above_median = 0
    runs_below_median = 0
    current_run = 1
    
    for i in range(1, n):
        if data[i] > median:
            if data[i - 1] <= median:
                runs_above_median += 1
            else:
                current_run += 1
        elif data[i] < median:
            if data[i - 1] >= median:
                runs_below_median += 1
            else:
                current_run += 1
    
    n1 = sum(1 for x in data if x > median)
    n2 = sum(1 for x in data if x < median)
    print(data)
    total_runs = runs_above_median + runs_below_median
    print(f"Total no.of runs:{total_runs}")
    print("No.of A's: ",n1)
    print("No.of B's: ",n2)
    print("enter the critical values:")
    critical_lower,critical_upper=3,11
    if(critical_lower>critical_upper):
        c=critical_lower
        critical_lower=critical_upper
        critical_upper=c
    
    if critical_lower <= total_runs <= critical_upper:
        print("Accept the null hypothesis (H0): The data is random.")
    else:
        print("Reject the null hypothesis (H0): The data is not random.")


csv_file_path = './diabetesdataset.csv'
with open(csv_file_path, 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)
    data = list(csv_reader)
    data1 = [float(row[0]) for row in data]  # Assuming the values are in the first column
    
sample_size = 14
if sample_size > len(data):
    sample_size= len(data)

random_samples = random.sample(data, sample_size)
sampledata1=[float(row[0])for row in random_samples]

runs_test(sampledata1)
