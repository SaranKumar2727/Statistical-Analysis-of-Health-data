import pandas as pd
import random
file_path = './diabetesdataset.csv'
data = pd.read_csv(file_path)
column1 = data['Outcome']
column2 = data['Age']
print("H0: P1=P2=P3 Proportions of pregnant women at different ages are equal")

print("H1: H0 is false")
print("\n")
related_data = list(zip(column1, column2))

num_samples = 100

random_samples = random.sample(related_data, num_samples)

print("Random samples:",random_samples)


count = [[0 for _ in range(3)] for _ in range(2)]

for a,b in random_samples:
    if a==0 and b<=25:
        count[0][0]+=1
    if a==1 and b<=25:
        count[1][0]+=1
    if a==0 and b>25 and b<=45:
        count[0][1]+=1
    if a==1 and b>25 and b<=45:
        count[1][1]+=1
    if a==0 and b>45 :
        count[0][2]+=1
    if a==1 and b>45:
        count[1][2]+=1


print("Contingency matrix:\n[")
for i in range(len(count)):
    print(count[i])
print("]")

row_totals = [sum(row) for row in count]

col_totals = [sum(col) for col in zip(*count)]

total = sum(row_totals)

expected = [[(row_total * col_total) / total for col_total in col_totals] for row_total in row_totals]

chi2 = sum([(observed - exp) ** 2 / exp for row, exp_row in zip(count, expected) for observed, exp in zip(row, exp_row)])

degrees_of_freedom = (len(row_totals) - 1) * (len(col_totals) - 1)

print("Chi-square statistic:", chi2)
print("Degrees of freedom:", degrees_of_freedom)

critical_value = 5.991 #alpha=0.05
print("critical value:",critical_value)
if chi2 > critical_value:
    print("Reject the null hypothesis")
else:
    print("Accept the null hypothesis")

