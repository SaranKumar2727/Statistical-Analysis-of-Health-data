import numpy as np
import pandas as pd
import scipy.stats as stats
import os

# Connecting the paths of code and dataset
file_path = './diabetesdataset.csv'  

# Check if the file exists
if os.path.exists(file_path):
    # Reading CSV file
    df = pd.read_csv(file_path)

    # Getting only one column with name = "glucose_after_lunch"  
    new_df = df['Glucose(after Lunch)']

    # To get p0
    new_df_len = len(new_df)
    filtered_df = new_df[new_df < 120]
    filtered_df_len = len(filtered_df)
    p0 = filtered_df_len / new_df_len
    n = 34
    
    random_df = new_df.sample(n=n, random_state=1)
    filtered_random = random_df[random_df < 120] 
    filtered_random_len = len(filtered_random)
    p = filtered_random_len / n

    

    # Functions
    def Z_cal(p, p0, n):
        diff_p = p - p0
        error = findError(p0, n)
        z_cal = diff_p / error
        return z_cal

    def findError(p0, n):
        q0 = 1 - p0
        pdt_pq = p0 * q0
        error = np.sqrt(pdt_pq / (n - 1))
        return error

    def Z_tab(A_ci):
        z_tab = 1.9600
        return z_tab

    def calcCI(p0, n):
        error = findError(p0, n)
        z_lower = p0 - z_tab * error
        z_upper = p0 + z_tab * error
        print("\nConfidence Interval : \n", z_lower, " <= p < ", z_upper)

    # Implementation
    # Hypothesis
    print("Hypothesis:\nH0 : p = 0.53125 (claim)\nH1 : p != 0.53125")
    print("population proportion: ",p0)

    print("Sample Proportion:", p)
    # Getting z calculated and tabulated values
    z_cal = Z_cal(p, p0, n)
    z_tab = Z_tab(0.05)

    print("z_cal :", z_cal)
    print("z_tab :", z_tab)

    # Summarizing results
    if z_cal <= z_tab:
        print("Since z_cal<=z_tab ==> Accept H0")
    else:
        print("\nReject H0")

    # Getting confidence interval
    calcCI(p0, n)
    
# Calculate sample means for plotting
    import numpy as np
    import matplotlib.pyplot as plt
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

