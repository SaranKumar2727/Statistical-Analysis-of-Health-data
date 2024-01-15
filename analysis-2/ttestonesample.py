import csv
import random
import statistics
import math
import scipy.stats as stats
import matplotlib.pyplot as plt
csv_file_path = './diabetesdataset.csv'
with open(csv_file_path, 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)
    data = list(csv_reader)
    data1 = [float(row[0]) for row in data]  # Assuming the values are in the first column
    
sample_size = 25
if sample_size > len(data):
    sample_size= len(data)

random_samples = random.sample(data, sample_size)
sampledata1=[float(row[0])for row in random_samples]
print("Sample: ",sampledata1)
def calculate_mean(data):
    return sum(data) / len(data)

def calculate_stddev(data):
    mean = calculate_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    stddev = math.sqrt(variance)
    return stddev

population_mean = calculate_mean(data1)
population_stddev = calculate_stddev(data1)
sample_mean=calculate_mean(sampledata1)
sample_stddev = calculate_stddev(sampledata1)
sample_means=[]
sample_means.append(sample_mean)
print(f"Population Mean: {population_mean}")
print(f"Population Standard Deviation: {population_stddev}")

print(f"sample Mean: {sample_mean}")
print(f"sample Standard Deviation: {sample_stddev}")

standard_error = population_stddev / math.sqrt(sample_size)
if(sample_size<=30):
    t_cal = abs(sample_mean - population_mean) / standard_error

    print("calculated t-value: ",t_cal)
    #let alpha=0.05
    alpha = 0.05 
    t_tab=2.064
    print("tabulated t-value: ",t_tab)
    if t_cal<=t_tab:
        print("Accept Claimed mean i.e null hypothesis")
        #confidence interval
        low_lim=sample_mean-(t_tab*(sample_stddev/(sample_size-1)**0.5))
        upp_lim=sample_mean+(t_tab*(sample_stddev/(sample_size-1)**0.5))
        print(f"confidence-interval: \t{low_lim}<mean<{upp_lim}")
    else:
        print("Reject Null hypothesis")


# Calculate sample means for plotting
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
  # Your z_tab value


# Generating data for the normal distribution curve
x = np.linspace(-4, 4, 1000)
y = stats.norm.pdf(x, 0, 1)  # Mean=0, Standard Deviation=1 for standard normal distribution

# Plotting the normal distribution curve
plt.plot(x, y, label='Standard Normal Distribution')

# Shading the area beyond z_tab
x_fill = np.linspace(t_tab, 4, 100)
y_fill = stats.norm.pdf(x_fill, 0, 1)
plt.fill_between(x_fill, y_fill, color='gray', alpha=0.3, label='Area beyond t_tab')

# Highlighting z_tab and z_cal values
plt.axvline(x=t_tab, color='red', linestyle='--', label='Critical t-value (t_tab)')
plt.text(t_tab + 0.1, 0.1, f't_tab = {t_tab}', color='red')

plt.axvline(x=t_cal, color='green', linestyle='--', label='Calculated t-value (t_cal)')
plt.text(t_cal + 0.1, 0.1, f't_cal = {t_cal}', color='green')

plt.xlabel('t-score')
plt.ylabel('Probability Density')
plt.title('Normal Distribution with t_tab and t_cal')
plt.legend()
plt.grid(True)
plt.show()