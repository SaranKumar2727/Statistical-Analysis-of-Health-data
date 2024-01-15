import numpy as np
import pandas as pd
import scipy.stats as stats
import os

# Connecting the paths of code and dataset
file_path = './diabetesdataset.csv' 

# Check if the file exists
if os.path.exists(file_path):
    # Reading CSV files
    after_df = pd.read_csv(file_path)
    before_df = pd.read_csv(file_path)

    # Extract the 'Glucose(after Lunch)' & 'Glucose(before Lunch)' column from each DataFrame
    after_glucose = after_df['Glucose(after Lunch)']
    before_glucose = before_df['Glucose(before Lunch)']

    # Sample _p1, _p2
    n1 = 34
    n2 = 38
    random_after_df = after_glucose.sample(n=n1, random_state=1)
    random_before_df = before_glucose.sample(n=n2, random_state=1)

    filtered_random_after = random_after_df[random_after_df < 120] 
    filtered_random_before = random_before_df[random_before_df < 120] 

    m1 = len(filtered_random_after)
    m2 = len(filtered_random_before)

    _p1 = m1 / n1
    _p2 = m2 / n2
    P = (m1 + m2) / (n1 + n2)

    # Functions
    # Calculate Z value
    def Z_cal(p1, p2, P, n1, n2):
        diff_p = abs(p1 - p2)
        error = findError(n1, n2, P)
        z_cal = diff_p / error
        return z_cal

    # Find error term
    def findError(n1, n2, P):
        Q = 1 - P
        pdt_PQ = P * Q
        sum_n1_n2 = (1/n1) + (1/n2)
        error = np.sqrt(pdt_PQ * sum_n1_n2)
        return error

    # Get Z tabulated value
    def Z_tab(A_ci):
        z_tab =1.9600
        return z_tab

    # Get confidence interval
    def calcCI(p1, p2, n1, n2, P):
        error = findError(n1, n2, P)
        diff_p = abs(p1 - p2)
        z_lower = diff_p - z_tab * error
        z_upper = diff_p + z_tab * error
        print("\n95% Confidence Interval:\n", z_lower, " <= p1-p2 <=", z_upper)

    # Implementation
    # Hypothesis
    print("Hypothesis:\nH0 : P1 = P2 (claim)\nH1 : P1 != P2")
    print("Sample proportion-p1: ",_p1)
    print("Sample proportion-p2: ",_p2)
    # Getting z calculated and tabulated values
    z_tab = Z_tab(0.05)
    z_cal = Z_cal(_p1, _p2, P, n1, n2)

    print("z_cal :", z_cal)
    print("z_tab :", z_tab)

    # Summarizing results
    if z_cal <= z_tab:
        print("Accept H0")
    else:
        print("Reject H0")

    # Getting confidence interval
    calcCI(_p1, _p2, n1, n2, P)

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


else:
    print(f"File not found: {file_path}")