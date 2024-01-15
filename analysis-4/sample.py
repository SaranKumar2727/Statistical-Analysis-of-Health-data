import pandas as pd
import random

# Load the CSV file into a pandas DataFrame
file_path = '../diabetesdataset.csv'  # Replace 'your_file.csv' with your actual file path
data = pd.read_csv(file_path)

# Assuming the CSV has columns named 'column1' and 'column2', change these to your actual column names
column1 = data['Outcome']
column2 = data['Glucose(after Lunch)']

# Combine the two columns into a list of tuples (assuming the columns are related)
related_data = list(zip(column1, column2))

# Define the number of random samples you want
num_samples = 100  # Change this to the number of samples you need

# Take random samples from the related data
random_samples = random.sample(related_data, num_samples)

print("Random samples:")
for sample in random_samples:
    print(sample)
# Your random_samples list containing tuples



count = [[0 for _ in range(3)] for _ in range(2)]

# Count the number of values in the second column where column A is 0 and column B is < 100
for a,b in random_samples:
    if a==0 and b<=100:
        count[0][0]+=1
    if a==1 and b<=100:
        count[1][0]+=1
    if a==0 and b>100 and b<=130:
        count[0][1]+=1
    if a==1 and b>100 and b<=130:
        count[1][1]+=1
    if a==0 and b>130 :
        count[0][2]+=1
    if a==1 and b>130:
        count[1][2]+=1
    
# count = sum(1 for a, b in random_samples if a == 0 and b < 100)

print("Count:", count)



# Calculate row and column totals
row_totals = [sum(row) for row in count]
col_totals = [sum(col) for col in zip(*count)]
total = sum(row_totals)

# Calculate expected frequencies under the assumption of independence
expected = [[(row_total * col_total) / total for col_total in col_totals] for row_total in row_totals]

# Calculate chi-square statistic
chi2 = sum([(observed - exp) ** 2 / exp for row, exp_row in zip(count, expected) for observed, exp in zip(row, exp_row)])

# Calculate degrees of freedom
degrees_of_freedom = (len(row_totals) - 1) * (len(col_totals) - 1)

print("Chi-square statistic:", chi2)
print("Degrees of freedom:", degrees_of_freedom)

# Critical value from chi-square distribution table for a chosen significance level (e.g., 0.05)
# Look up the critical value based on degrees_of_freedom and your chosen significance level in a chi-square distribution table
# For example, for 1 degree of freedom and a significance level of 0.05, the critical value is approximately 3.8415

critical_value = 3.8415  # Replace this with the critical value from the chi-square distribution table

# Compare chi-square statistic with critical value
if chi2 > critical_value:
    print("Reject the null hypothesis: Variables are dependent")
else:
    print("Fail to reject the null hypothesis: Variables are independent")

