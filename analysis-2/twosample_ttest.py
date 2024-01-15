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
    data1 = [float(row[1]) for row in data]  # Assuming the values are in the 2 and 3 column
    data2 = [float(row[2]) for row in data]
    
sample_size1 = 15

sample_size2 = 14

random_samples1 = random.sample(data, sample_size1)
random_samples2 = random.sample(data, sample_size2)
sampledata1=[float(row[0])for row in random_samples1]
sampledata2=[float(row[0])for row in random_samples2]

print("sample-1: ",sampledata1)
print("sample-2: ",sampledata2)
def calculate_mean(data):
    return sum(data) / len(data)

def calculate_stddev(data):
    mean = calculate_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    stddev = math.sqrt(variance)
    return stddev
population_mean = calculate_mean(data1)
population_stddev = calculate_stddev(data1)
sample_stddev1 = calculate_stddev(sampledata1)
sample_stddev2 = calculate_stddev(sampledata2)
sample_mean1= calculate_mean(sampledata1)
sample_mean2= calculate_mean(sampledata2)

print(f"Population Mean: {population_mean}")
print(f"Population Standard Deviation: {population_stddev}")

print(f"sample1 Mean: {sample_mean1}")
print(f"sample1 Standard Deviation: {sample_stddev1}")
print(f"sample2 Mean: {sample_mean2}")
print(f"sample2 Standard Deviation: {sample_stddev2}")


standard_error =math.sqrt((sample_stddev1**2/sample_size1)+(sample_stddev2**2/sample_size2)) 

# Calculate the Z-score
t_cal = abs(sample_mean1 - sample_mean2) / standard_error
alpha = 0.05
  # Your t_tab value
df = (sample_size1+sample_size2) - 2

t_tab = 2.052

print("t-calculated: ",t_cal)
print("t-tabulated: ",t_tab)
if t_cal <= t_tab:
    print("since tcal<=ttab => accept the null hypothesis")
else:
    print("since tcal>ttab => reject the null hypothesis")

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

x = np.linspace(-4, 4, 1000)
y = stats.norm.pdf(x, 0, 1)  # Mean=0, Standard Deviation=1 for standard normal distribution

# Plotting the normal distribution curve
plt.plot(x, y, label='Standard Normal Distribution')

# Shading the area beyond t_tab
x_fill = np.linspace(t_tab, 4, 100)
y_fill = stats.norm.pdf(x_fill, 0, 1)
plt.fill_between(x_fill, y_fill, color='gray', alpha=0.3, label='Area beyond t_tab')

# Highlighting t_tab and t_cal values
plt.axvline(x=t_tab, color='red', linestyle='--', label='Critical z-value (t_tab)')
plt.text(t_tab + 0.1, 0.1, f't_tab = {t_tab}', color='red')

plt.axvline(x=t_cal, color='green', linestyle='--', label='Calculated z-value (t_cal)')
plt.text(t_cal + 0.1, 0.1, f't_cal = {t_cal}', color='green')

plt.xlabel('Z-score')
plt.ylabel('Probability Density')
plt.title('Normal Distribution with t_tab and t_cal')
plt.legend()
plt.grid(True)
plt.show()