# this is using this (x^2+Y^2-1)-(X^2)(Y^3)=0
import numpy as np
import matplotlib.pyplot as plt

# Create a grid of x and y values
x = np.linspace(-1.5, 1.5, 400)
y = np.linspace(-1.5, 1.5, 400)
X, Y = np.meshgrid(x, y)

# Define the equation
F = (X**2 + Y**2 - 1)**3 - X**2 * Y**3

# Plot the contour where F=0
plt.contour(X, Y, F, levels=[0], colors='red')
plt.title("Heart Shape: $(x^2 + y^2 - 1)^3 - x^2 y^3 = 0$")
plt.xlabel('x')
plt.ylabel('y')
plt.gca().set_aspect('equal')  # Equal aspect ratio for proper scaling
plt.show()
