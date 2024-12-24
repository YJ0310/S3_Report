import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress

def main():

    # Read the CSV file
    motor_oil_data = pd.read_csv("motor_oil.csv", sep="\t")
    motor_oil_data = motor_oil_data.loc[:, ~motor_oil_data.columns.str.contains('^Unnamed')].dropna()

    # Extracting the necessary columns
    log_T = motor_oil_data['log (T) '].to_numpy()
    delta_log_T = motor_oil_data['Δlog (T) '].to_numpy()
    log_log_v_plus_0_8 = motor_oil_data['log {log (v + 0.8)}'].to_numpy()
    delta_log_log_v_plus_0_8 = motor_oil_data['Δlog {log (v + 0.8)}'].to_numpy()

    # Least squares fit
    slope, intercept, r_value, p_value, std_err = linregress(log_T, log_log_v_plus_0_8)
    poly = np.poly1d([slope, intercept])
    fit_values = poly(log_T)

    # Centroid
    centroid_x = np.mean(log_T)
    centroid_y = np.mean(log_log_v_plus_0_8)

    # Intercept
    intercept_x = 0
    intercept_y = poly(intercept_x)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.errorbar(log_T, log_log_v_plus_0_8, xerr=delta_log_T, yerr=delta_log_log_v_plus_0_8, fmt='bo', label='y-values')
    plt.plot(log_T, fit_values, 'r-', label='Least-square Gradient')
    plt.plot(centroid_x, centroid_y, 'ks', label='Centroid')

    # Labels and title
    plt.xlabel('log(T)')
    plt.ylabel('log{log(v + 0.8)}')
    plt.title('Motor Oil: Least-squares graph of log{log(v + 0.8)} against log(T)')

    # Legend
    plt.legend()

    # Grid and show plot
    plt.grid(True)
    plt.show()

    # Print gradient and its uncertainty
    print(f'Gradient (slope): {slope:.4f}')
    print(f'Uncertainty (standard error): {std_err:.4f}')
    input("\n\nPress Enter To Continue:\n")
