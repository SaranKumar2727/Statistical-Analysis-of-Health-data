import numpy as np 
import pandas as pd
import os

file_path = './Diabetesdataset.csv'

if os.path.exists(file_path):

    df = pd.read_csv(file_path)

    glucose_after_lunch = df['Glucose(after Lunch)']

    filtered_data = glucose_after_lunch[glucose_after_lunch < 110]

    p0 = len(filtered_data) / len(glucose_after_lunch)
    print("P0: ",p0)

    margin_of_error = 0.2 #20% margin of error
    alpha = 0.05

    def calculate_sample_size(p0, margin_of_error, alpha):
        z_tab = 1.9600
        q0 = 1 - p0
        required_sample_size = ((z_tab ** 2) * p0 * q0) / (margin_of_error ** 2)
        return int(np.ceil(required_sample_size))

    sample_size = calculate_sample_size(p0, margin_of_error, alpha)
    print(f"Estimated sample size: {sample_size}")

else:
    print(f"File not found: {file_path}")