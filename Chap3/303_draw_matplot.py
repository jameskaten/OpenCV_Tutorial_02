# Import required libraries
import matplotlib.pyplot as plt    # Matplotlib for plotting graphs
import numpy as np                 # NumPy library for numerical operations

# Create a NumPy array with sample data points
# This creates a 1-dimensional array with 8 values
a = np.array([2,6,7,3,12,8,4,5])

# Create a line plot of the array
# By default, plt.plot will use the array indices (0-7) as x-coordinates
# and the array values as y-coordinates
plt.plot(a)

# Display the plot
# This command opens a window showing the graph
plt.show()