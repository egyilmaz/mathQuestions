import matplotlib.pyplot as plt
import numpy as np

# Original coordinates of the triangle
x = [1, 3, 2]
y = [2, 2, 4]

# Angle of rotation in degrees (change as needed)
angle_degrees = 90

# Convert angle to radians
angle_radians = np.radians(angle_degrees)

# Rotation matrix
cos_theta = np.cos(angle_radians)
sin_theta = np.sin(angle_radians)
rotation_matrix = np.array([[cos_theta, -sin_theta], [sin_theta, cos_theta]])

# Apply the rotation matrix to each vertex to get new coordinates
original_vertices = np.array([x, y])
new_vertices = np.dot(rotation_matrix, original_vertices)

# Extract the new x and y coordinates of the rotated triangle
new_x, new_y = new_vertices

# Create a plot
plt.figure(figsize=(6, 6))
plt.plot(new_x.tolist() + [new_x[0]], new_y.tolist() + [new_y[0]], marker='o', linestyle='-')

# Set axis limits centered at (0, 0)
plt.xlim(-5, 5)
plt.ylim(-5, 5)

# Draw X and Y axes with zero at the intersection
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Set bottom and left spines as x and y axes of coordinate system
plt.gca().spines['bottom'].set_position('zero')
plt.gca().spines['left'].set_position('zero')

# Remove top and right spines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Create 'x' and 'y' labels placed at the end of the axes
plt.xlabel('x', size=14, labelpad=-24, x=1.03)
plt.ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)

# Show the plot
plt.grid(True)
plt.show()