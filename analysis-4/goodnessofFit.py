
import random
import matplotlib.pyplot as plt
from scipy.stats import chi2
import pandas as pd

def chi_squared_statistic(observed, expected):
    return sum((obs - exp) ** 2 / exp for obs, exp in zip(observed, expected))


def goodnessofFit(observed, expected, alpha=0.05):
    test_statistic = chi_squared_statistic(observed, expected)
    df = len(observed) - 1
    critical_val=chi2.ppf(1 - alpha, df)

    if test_statistic<=critical_val:
        result = "Accept the H0 i.e the data is good fit"
    else:
        result = "Reject the H0"

    print(f"Test Statistic: {test_statistic}")
    print(f"Critical-value: {critical_val}")
    print(f"Result: {result}")

df = pd.read_csv('./diabetesdataset.csv')
sample_size = 100

sampledata1 = random.sample(df['Glucose(before Lunch)'].tolist(), sample_size)
print(sampledata1)
observed=[0]*5

for i in sampledata1:
    if(i<=80.0):
        observed[0]+=1
for i in sampledata1:
    if(i>80.0 and i<=100.0):
        observed[1]+=1
for i in sampledata1:
    if(i>100.0 and i<=120.0):
        observed[2]+=1
for i in sampledata1:
    if(i>120.0 and i<=140.0):
        observed[3]+=1
for i in sampledata1:
    if(i>140):
        observed[4]+=1


print("observed data: ",observed)
expected_data = [val + random.randint(-5, 5) for val in observed]
for i in expected_data:
    if i==0.0:
        i=1.0
print("expected data: ",expected_data)
goodnessofFit(observed, expected_data)

x_values = range(len(observed))

plt.figure(figsize=(8, 6))

# Plot observed data
plt.plot(x_values, observed, label='Observed data', marker='o', linestyle='-', color='blue')

# Plot expected data
plt.plot(x_values, expected_data, label='Expected data', marker='x', linestyle='--', color='red')

# Add labels and title
plt.xlabel('Index')
plt.ylabel('Values')
plt.title('Observed vs Expected Data')

# Show legend
plt.legend()

# Show plot
plt.show()