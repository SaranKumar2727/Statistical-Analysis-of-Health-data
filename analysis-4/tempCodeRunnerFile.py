import pandas as pd
import random

def withoutYates(count,n):
    a=count[0][0]
    b=count[0][1]
    c=count[1][0]
    d=count[1][1]
    test_stat=(n*((a*d)-(b*c))**2)/((a+b)*(a+c)*(b+d)*(c+d))
    return test_stat
def YatesCorrection(count,n):
    a=count[0][0]
    b=count[0][1]
    c=count[1][0]
    d=count[1][1]
    test_stat=(n*((abs(a*d-b*c)-n/2)**2))/((a+b)*(a+c)*(b+d)*(c+d))
    return test_stat
file_path = './diabetesdataset.csv'
data = pd.read_csv(file_path)
column1 = data['Outcome']
column2 = data['Age']
print("H0: P1=P2=P3")
print("H1: H0 is false")
print("\n")
related_data = list(zip(column1, column2))

num_samples = 100

random_samples = random.sample(related_data, num_samples)

print("Random samples:",random_samples)


count = [[0 for _ in range(2)] for _ in range(2)]

for a,b in random_samples:
    if a==0 and b<=25:
        count[0][0]+=1
    if a==1 and b<=25:
        count[1][0]+=1
    if a==0 and b>25:
        count[0][1]+=1
    if a==1 and b>25:
        count[1][1]+=1
    


print("Contingency matrix:\n[")
for i in range(len(count)):
    print(count[i])
print("]")

flag=0
for i in range(2):
    for j in range(2):
        if(count[i][j]<5):
            flag=1
            break
if(flag==0):
    print("since all the contingency values are >=5, applying the 2x2 contingency without yates correction")
    test_stat=withoutYates(count,num_samples)
else:
    print("since one of the contingency values are <5, applying the 2x2 contingency with yates correction")
    test_stat=YatesCorrection(count,num_samples)


degrees_of_freedom = 1

print("Chi-square statistic:", test_stat)
print("Degrees of freedom:", degrees_of_freedom)

critical_value = 3.841 #alpha=0.05

if test_stat > critical_value:
    print("Reject the null hypothesis")
else:
    print("Accept the null hypothesis")

