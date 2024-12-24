import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress

def main():

    # Read the CSV file
    glycerol_graph1 = pd.read_csv("glycerol_parta.csv", sep="\t")
    glycerol_graph1 = glycerol_graph1.loc[:, ~glycerol_graph1.columns.str.contains('^Unnamed')].dropna()

    # Extract data from the DataFrame
    t = glycerol_graph1['Time taken for 50ml aqueous glycerol to flow (s)'].to_numpy()
    v = glycerol_graph1['Kinematic viscosity, v (10⁻² cm² s⁻¹)'].to_numpy()

    # Least squares fit
    slope, intercept, r_value, p_value, std_err = linregress(t, v)
    poly = np.poly1d([slope, intercept])
    v_fit = poly(t)

    # Centroid
    centroid_t = np.mean(t)
    centroid_v = np.mean(v)

    # Intercept
    intercept_t = 0
    intercept_v = poly(intercept_t)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(t, v, 'm^', label='y-values')
    plt.plot(t, v_fit, 'r-', label='Least-square Gradient')
    plt.plot(centroid_t, centroid_v, 'ks', label='Centroid')
    plt.plot(intercept_t, intercept_v, 'cs', label='Intercept')


    # Labels and title
    plt.xlabel('Time, $t$ (s)')
    plt.ylabel('Kinematic viscosity, $v \\times 10^{-2} \\, (cm^2 s^{-1})$')
    plt.title('Glycerol: Least-square graph of $v$ against $t$')

    # Legend
    plt.legend()

    # Grid and show plot
    plt.grid(True)
    plt.show()

    # Print gradient and its uncertainty
    print(f'Gradient (slope): {slope:.4f}')
    print(f'Uncertainty (standard error): {std_err:.4f}')
    input("\n\nPress Enter To Continue:\n")
    