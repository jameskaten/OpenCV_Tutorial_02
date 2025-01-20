# Import required libraries
import matplotlib.pyplot as plt    # Matplotlib for plotting graphs
import numpy as np                 # NumPy library for numerical operations

# Create x-axis data points using numpy.arange
# np.arange(10) creates an array of integers from 0 to 9
x = np.arange(10)

# Create y-axis data points by squaring x values
# This creates the array [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
y = x**2

# Create a line plot with x and y coordinates
# plt.plot(x, y) draws a line connecting points with x,y coordinates
plt.plot(x, y)

# Display the plot
# This command opens a window showing the graph
plt.show()