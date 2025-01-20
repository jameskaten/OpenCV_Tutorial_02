# Import required libraries
import matplotlib.pyplot as plt    # Matplotlib for plotting graphs
import numpy as np                 # NumPy library for numerical operations

# Create x-axis data points using numpy.arange
# np.arange(10) creates an array of integers from 0 to 9
x = np.arange(10)

# Create three different functions for plotting
f1 = x+5      # Linear function: adds 5 to each x value
f2 = x**2     # Quadratic function: squares each x value
f3 = x**2 + x*2   # Quadratic function with linear term: x² + 2x

# Create multiple plots with different line styles
plt.plot(x, 'r--')   # Plot x vs index with red dashed line ('r--')
plt.plot(f1, 'g.')   # Plot f1 vs index with green dots ('g.')
plt.plot(f2, 'bv')   # Plot f2 vs index with blue triangular markers ('bv')
plt.plot(f3, 'ks')   # Plot f3 vs index with black square markers ('ks')

# Display all plots in the same figure
# This command opens a window showing all graphs overlaid
plt.show()
