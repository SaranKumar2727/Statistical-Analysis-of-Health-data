import numpy as np
import pandas as pd
file_path = './diabetesdataset.csv'  


df = pd.read_csv(file_path)

population_glucose = df['Glucose(after Lunch)']

var = np.std(population_glucose)
margin_of_error = 12
alpha, beta = 0.05, 0.10
power=1-beta

def calculate_sample_size(var, margin_of_error):
    z_a_tab = 1.9600
    z_power = 1.282
    required_sample_size = ((2 * var * (z_a_tab + z_power)) / margin_of_error)**2
    return int(np.ceil(required_sample_size) // 2) 

estimated_sample_size = calculate_sample_size(var, margin_of_error)
print("Estimated sample size for 2 samples(n1+n2) =", estimated_sample_size)
print("Estimated sample size for each sample =", estimated_sample_size//2+1)
