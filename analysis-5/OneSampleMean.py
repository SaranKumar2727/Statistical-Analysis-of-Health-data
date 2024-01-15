import numpy as np 
import pandas as pd
import scipy.stats as stats
import os

# Set the file path
file_path = './diabetesdataset.csv'

# Check if the file exists
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    blood_glucose_level = df['Glucose(after Lunch)']
    population_mean=np.mean(blood_glucose_level)
    population_std = np.std(blood_glucose_level)
    print("population mean: ",population_mean)
    margin_of_error = 12 #10% margin of error with population mean
    alpha = 0.05  

    def calculate_sample_size(population_std, margin_of_error, alpha):
        z_tab = 1.9600
        required_sample_size = ((z_tab * population_std) / margin_of_error)**2
        return int(np.ceil(required_sample_size))

    sample_size = calculate_sample_size(population_std, margin_of_error, alpha)
    print(f"Estimated sample size: {sample_size}")

else:
    print(f"File not found: {file_path}")