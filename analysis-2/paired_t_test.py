from matplotlib import pyplot as plt
import pandas as pd
from scipy import stats
import random
import numpy as np

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
print(differences)
# Calculate the mean and standard deviation of the differences
mean_diff = sum(differences) / len(differences)
std_dev_diff = np.sqrt(sum((diff - mean_diff) ** 2 for diff in differences) / (len(differences) - 1))

# Calculate the standard error of the mean difference
standard_error = std_dev_diff / np.sqrt(len(differences))

# Calculate t-statistic
t_cal = mean_diff / standard_error

# Degrees of freedom
df = len(differences) - 1


alpha = 0.05
t_tab=2.365
print("calculated t-value: ",t_cal)
print("tabulated t-value: ",t_tab)

if t_cal>t_tab:
    print("Reject the null hypothesis i.e mean difference !=0")
else:
    print("Fail to reject the null hypothesis i.e mean difference == 0")

# Calculate 95% Confidence Interval for the Mean Difference
ci_mean_diff = stats.t.interval(0.95, len(differences) - 1, loc=mean_diff, scale=stats.sem(differences))
print(f"Confidence Interval: {ci_mean_diff}")
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
