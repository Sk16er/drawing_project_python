import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate the heart shape
t = np.linspace(0, 2 * np.pi, 100)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
z = np.sin(t)  # Adding a third dimension for 3D effect

# Plot the heart shape
ax.plot(x, y, z, color='red')

# Add text
ax.text(0, 0, 0, "I love you", color='red', fontsize=20, ha='center')

# Set the labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set the limits
ax.set_xlim([-20, 20])
ax.set_ylim([-20, 20])
ax.set_zlim([-2, 2])

# Show the plot
plt.show()
