import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress

def main(): 
        
    # Read the CSV files
    motor_oil_data = pd.read_csv("motor_oil.csv", sep="\t")
    motor_oil_data = motor_oil_data.loc[:, ~motor_oil_data.columns.str.contains('^Unnamed')].dropna()
    hydraulic_oil_data = pd.read_csv("hydraulic_oil.csv", sep="\t")
    hydraulic_oil_data = hydraulic_oil_data.loc[:, ~hydraulic_oil_data.columns.str.contains('^Unnamed')].dropna()

    # Extracting the necessary columns
    log_T_motor = motor_oil_data['log (T) '].to_numpy()
    log_log_v_plus_0_8_motor = motor_oil_data['log {log (v + 0.8)}'].to_numpy()

    log_T_hydraulic = hydraulic_oil_data['log (T) '].to_numpy()
    log_log_v_plus_0_8_hydraulic = hydraulic_oil_data['log {log (v + 0.8)}'].to_numpy()

    # Least squares fit using linregress for motor oil
    slope_motor, intercept_motor, r_value_motor, p_value_motor, std_err_motor = linregress(log_T_motor, log_log_v_plus_0_8_motor)

    # Least squares fit using linregress for hydraulic oil
    slope_hydraulic, intercept_hydraulic, r_value_hydraulic, p_value_hydraulic, std_err_hydraulic = linregress(log_T_hydraulic, log_log_v_plus_0_8_hydraulic)

    # Define the range for plotting the lines
    log_T_range = np.linspace(0, 3.5, 100)

    # Calculate the fit lines
    fit_values_motor = slope_motor * log_T_range + intercept_motor
    fit_values_hydraulic = slope_hydraulic * log_T_range + intercept_hydraulic

    # Find the intercept point of the two lines
    A = np.array([[slope_motor, -1], [slope_hydraulic, -1]])
    b = np.array([-intercept_motor, -intercept_hydraulic])
    intercept_point = np.linalg.solve(A, b)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(log_T_range, fit_values_motor, 'r-', label='Motor Oil Least-square Gradient')
    plt.plot(log_T_range, fit_values_hydraulic, 'b-', label='Hydraulic Oil Least-square Gradient')
    plt.plot(intercept_point[0], intercept_point[1], 'ks', label='Intercept Point')

    # Draw the horizontal line at y=0
    plt.axhline(y=0, color='gray', linestyle='--')

    # Labels and title
    plt.xlabel('log(T)')
    plt.ylabel('log{log(v + 0.8)}')
    plt.title('Comparison of log{log(v + 0.8)} against log(T) for Motor and Hydraulic Oil')

    # Legend
    plt.legend()

    # Grid and show plot
    plt.grid(True)
    plt.show()

    # Print gradients and their uncertainties
    print("Motor Oil:")
    print(f'Gradient (slope): {slope_motor:.4f}')
    print(f'Intercept: {intercept_motor:.4f}')

    print("\nHydraulic Oil:")
    print(f'Gradient (slope): {slope_hydraulic:.4f}')
    print(f'Intercept: {intercept_hydraulic:.4f}')

    print("\nIntercept Point:")
    print(f'log(T): {intercept_point[0]:.4f}')
    print(f'log(log(v + 0.8)): {intercept_point[1]:.4f}')
    input("\n\nPress Enter To Continue:\n")
