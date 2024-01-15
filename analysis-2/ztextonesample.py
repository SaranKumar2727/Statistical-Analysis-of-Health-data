import csv
import random
import statistics
import math
import matplotlib.pyplot as plt

csv_file_path = './diabetesdataset.csv'

# Read data from CSV
with open(csv_file_path, 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)
    data = list(csv_reader)
    data1 = [float(row[0]) for row in data]  # Assuming the values are in the first column

# Sample size and random sampling
sample_size = 35
if sample_size > len(data):
    sample_size = len(data)

# Calculate sample mean and standard deviation
random_samples = random.sample(data, sample_size)
sampledata1 = [float(row[0]) for row in random_samples]
sample_mean = statistics.mean(sampledata1)
sample_stddev = statistics.stdev(sampledata1)
print("sample data: ",sampledata1)
# Calculate population mean and standard deviation
population_mean = statistics.mean(data1)
population_stddev = statistics.stdev(data1)

# Calculate standard error and z-value for z-test
standard_error = population_stddev / math.sqrt(sample_size)
z_cal = abs(sample_mean - population_mean) / standard_error

print(f"Population Mean: {population_mean}")
print(f"Population Standard Deviation: {population_stddev}")
print(f"Sample Mean: {sample_mean}")
print(f"Sample Standard Deviation: {sample_stddev}")
print(f"Calculated z-value: {z_cal}")
# Conduct hypothesis testing
alpha = 0.05
z_tab = 1.9600
print(f"Tabulated z-value: {z_tab}")
if z_cal <= z_tab:
    print("Accept Claimed mean i.e null hypothesis(H0)")
    low_lim = sample_mean - (z_tab * (sample_stddev / (sample_size - 1) ** 0.5))
    upp_lim = sample_mean + (z_tab * (sample_stddev / (sample_size - 1) ** 0.5))
    print(f"Confidence interval:\t{low_lim} < mean < {upp_lim}")
else:
    print("Reject Null hypothesis")

# Calculate sample means for plotting
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

z_tab = 1.9600  # Your z_tab value


# Generating data for the normal distribution curve
x = np.linspace(-4, 4, 1000)
y = stats.norm.pdf(x, 0, 1)  # Mean=0, Standard Deviation=1 for standard normal distribution

# Plotting the normal distribution curve
plt.plot(x, y, label='Standard Normal Distribution')

# Shading the area beyond z_tab
x_fill = np.linspace(z_tab, 4, 100)
y_fill = stats.norm.pdf(x_fill, 0, 1)
plt.fill_between(x_fill, y_fill, color='gray', alpha=0.3, label='Area beyond z_tab')

# Highlighting z_tab and z_cal values
plt.axvline(x=z_tab, color='red', linestyle='--', label='Critical z-value (z_tab)')
plt.text(z_tab + 0.1, 0.1, f'z_tab = {z_tab}', color='red')

plt.axvline(x=z_cal, color='green', linestyle='--', label='Calculated z-value (z_cal)')
plt.text(z_cal + 0.1, 0.1, f'z_cal = {z_cal}', color='green')

plt.xlabel('Z-score')
plt.ylabel('Probability Density')
plt.title('Normal Distribution with z_tab and z_cal')
plt.legend()
plt.grid(True)
plt.show()
