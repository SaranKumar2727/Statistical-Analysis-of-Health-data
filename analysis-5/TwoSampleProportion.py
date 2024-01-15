import numpy as np
import pandas as pd
import scipy.stats as stats
import os

df = pd.read_csv('./diabetesdataset.csv')


afterlunch_glucose = df['Glucose(after Lunch)']
beforelunch_glucose = df['Glucose(before Lunch)']

n1, n2 = len(afterlunch_glucose), len(beforelunch_glucose)
filtered_after = afterlunch_glucose[afterlunch_glucose < 120] 
filtered_before = beforelunch_glucose[beforelunch_glucose < 120] 

m1, m2 = len(filtered_after), len(filtered_before)
P1, P2 = m1 / n1, m2 / n2  
print("P1 :",P1)
print("P2 :",P2)
margin_of_error = 0.2
print("Margin of error:", margin_of_error)

alpha, beta = 0.05, 0.10 


def calculate_sample_size(P1, P2, margin_of_error):
    z_a_tab = 1.9600
    z_b_tab = 1.282

    P = (P1 + P2) / 2
    Q = 1 - P
    z_val = (2 * (z_a_tab + z_b_tab)) ** 2

    required_sample_size = (z_val * P * Q) / (margin_of_error ** 2)

    return int(np.ceil(required_sample_size) // 2)

estimated_sample_size = calculate_sample_size(P1, P2, margin_of_error, alpha, beta)
print("Estimated sample size for 2 samples =", estimated_sample_size)
print("Estimated sample size for each sample=",(estimated_sample_size)//2+(estimated_sample_size)%2)
