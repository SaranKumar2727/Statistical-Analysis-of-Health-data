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
    
sample_size1 = 35

sample_size2 = 40

random_samples1 = random.sample(data, sample_size1)
random_samples2 = random.sample(data, sample_size2)
sampledata1=[float(row[0])for row in random_samples1]
sampledata2=[float(row[0])for row in random_samples2]

print("Sample 1: ",sampledata1)
print("Sample 2: ",sampledata2)
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
z_cal = abs(sample_mean1 - sample_mean2) / standard_error
alpha = 0.05
z_tab=1.9600

print("z-calculated: ",z_cal)
if z_cal <= z_tab:
    print("since zcal<=ztab => accept the null hypothesis i.e claimed mean is true")
else:
    print("since zcal>ztab => reject the null hypothesis i.e claimed mean is not true")
# sample_means={sample_mean1,sample_mean2}
# sample_labels = [f'Sample {i + 1}' for i in range(len(sample_means))]

# plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
# plt.plot(sample_labels, p_values, color='skyblue', marker='o', linestyle='-')

# plt.xlabel('Sample')
# plt.ylabel('p-value')
# plt.title('two sample Z-Test p-values for Each Sample')

# alpha = 0.05  # Adjust as needed
# plt.axhline(y=alpha, color='red', linestyle='--', label=f'Significance Level (alpha = {alpha})')
# plt.legend()

# # Show the plot
# plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
# plt.tight_layout()  # Ensure labels fit within the figure
# plt.show()
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