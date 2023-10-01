import numpy as np
import matplotlib.pyplot as plt

def draw_triangle(x,y):
    plt.plot(x + [x[0]], y + [y[0]], marker='o', linestyle='-')


def cartesian(xmin, xmax, ymin, ymax):
    ticks_frequency = 2
    # Plot points
    fig, ax = plt.subplots(figsize=(8, 8))
    # Set identical scales for both axes
    ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')
    # Set bottom and left spines as x and y axes of coordinate system
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    # Create 'x' and 'y' labels placed at the end of the axes
    ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
    ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)
    # Create custom major ticks to determine position of tick labels
    x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
    y_ticks = np.arange(ymin, ymax+1, ticks_frequency)
    ax.set_xticks(x_ticks[x_ticks != 0])
    ax.set_yticks(y_ticks[y_ticks != 0])
    # Create minor ticks placed at each integer to enable drawing of minor grid
    # lines: note that this has no effect in this example with ticks_frequency=1
    ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
    ax.set_yticks(np.arange(ymin, ymax+1), minor=True)
    # Draw major and minor grid lines
    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
    # Draw arrows
    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)

    xs = [0]
    ys = [0]
    colors = ['m']
    # Plot points
    ax.scatter(xs, ys, c=colors)

    return fig, ax

def rotate(x, y, angle_degrees, rot_point=(0,0)):
    rot_point_x, rot_point_y = rot_point
    # Convert angle to radians
    angle_radians = np.radians(angle_degrees)

    # Translation matrix to move the rotation point to the origin
    translation_matrix1 = np.array([[1, 0, -rot_point_x],
                                    [0, 1, -rot_point_y],
                                    [0, 0, 1]])

    # Rotation matrix
    cos_theta = np.cos(angle_radians)
    sin_theta = np.sin(angle_radians)
    rotation_matrix = np.array([[cos_theta, -sin_theta, 0],
                                [sin_theta, cos_theta, 0],
                                [0, 0, 1]])

    # Translation matrix to move the rotation point back to its original position
    translation_matrix2 = np.array([[1, 0, rot_point_x],
                                    [0, 1, rot_point_y],
                                    [0, 0, 1]])

    # Combine the transformations
    transformation_matrix = np.dot(translation_matrix2, np.dot(rotation_matrix, translation_matrix1))

    # Apply the transformation to each vertex
    original_vertices = np.vstack((x, y, np.ones(len(x))))
    new_vertices = np.dot(transformation_matrix, original_vertices)

    # Extract the new x and y coordinates of the rotated triangle
    new_x, new_y, _ = new_vertices
    return new_x, new_y