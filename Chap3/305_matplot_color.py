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
# The 'r' argument specifies the color as red
# Other basic color codes: 'b' (blue), 'g' (green), 'k' (black), 
# 'y' (yellow), 'm' (magenta), 'c' (cyan), 'w' (white)
plt.plot(x, y, 'r')

# Display the plot
# This command opens a window showing the graph
plt.show()