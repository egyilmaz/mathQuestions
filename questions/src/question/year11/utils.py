import numpy as np
import matplotlib.pyplot as plt


class Vector():
    def __init__(self, x_start, y_start, x_end, y_end, color='blue'):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.color = color

    def draw(self, ax):
        hw = 0.2
        hl = 0.3
        ax.arrow(self.x_start, self.y_start, self.x_end - self.x_start, self.y_end - self.y_start, head_width=hw, head_length=hl, fc=self.color, ec=self.color, length_includes_head=True)

    def add(self, v2, color='red'):
        v1_x_comp = self.x_end - self.x_start
        v1_y_comp = self.y_end - self.y_start
        v2_x_comp = v2.x_end - v2.x_start
        v2_y_comp = v2.y_end - v2.y_start
        total_x = v1_x_comp + v2_x_comp
        total_y = v1_y_comp + v2_y_comp
        return Vector(self.x_start, self.y_start, self.x_start+total_x, self.y_start+total_y, color=color)

def draw_line(ax, start_x, start_y, end_x, end_y):
    ax.arrow(start_x, start_y, end_x - start_x, end_y - start_y)

def draw_triangle(x,y):
    plt.plot(x + [x[0]], y + [y[0]], marker='o', linestyle='-')

def draw_rectangle(x,y):
    plt.plot(x + [x[0]], y + [y[0]], marker='o', linestyle='-')

def cartesian(xmin, xmax, ymin, ymax, ticks=None):
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
    if ticks == None:
        x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
        y_ticks = np.arange(ymin, ymax+1, ticks_frequency)
        ax.set_xticks(x_ticks[x_ticks != 0])
        ax.set_yticks(y_ticks[y_ticks != 0])
        # Create minor ticks placed at each integer to enable drawing of minor grid
        # lines: note that this has no effect in this example with ticks_frequency=1
        ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
        ax.set_yticks(np.arange(ymin, ymax+1), minor=True)
    else: 
        x_ticks = ticks[0]
        y_ticks = ticks[1]
        ax.set_xticks(x_ticks)
        ax.set_yticks(y_ticks)

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