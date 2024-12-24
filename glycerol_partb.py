import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress

def main():
    # Read the CSV file
    glycerol_graph2 = pd.read_csv("glycerol_partb.csv", sep="\t")
    glycerol_graph2 = glycerol_graph2.loc[:, ~glycerol_graph2.columns.str.contains('^Unnamed')].dropna()

    # Example data - replace with your own data
    # Data points
    x = glycerol_graph2['1/t² (s⁻²)'].to_numpy()
    y = glycerol_graph2['v/t (m²/s⁻²)'].to_numpy()

    print(x)
    print(y)

    # Least squares fit
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    poly = np.poly1d([slope, intercept])
    fit_values = poly(x)

    # Centroid
    centroid_x = np.mean(x)
    centroid_y = np.mean(y)

    # Intercept
    intercept_x = 0
    intercept_y = poly(intercept_x)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'm^', label='y-values')
    plt.plot(x, fit_values, 'r-', label='Least-square Gradient')
    plt.plot(centroid_x, centroid_y, 'ks', label='Centroid')
    plt.plot(intercept_x, intercept_y, 'cs', label='Intercept')


    # Labels and title
    plt.xlabel('Kinematic viscosity over time, $\\frac{\\nu}{t}$ (cm² s⁻²)')
    plt.ylabel('One over time squared, $\\frac{1}{t^2}$ (s⁻²)')
    plt.title('Glycerol: Least-square graph of $\\frac{\\nu}{t}$ against $\\frac{1}{t^2}$')

    # Legend
    plt.legend()

    # Grid and show plot
    plt.grid(True)
    plt.show()

    # Print gradient and its uncertainty
    print(f'Gradient (slope): {slope:.4f}')
    print(f'Uncertainty (standard error): {std_err:.4f}')
    input("\n\nPress Enter To Continue:\n")
