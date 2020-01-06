from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity
import random
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import



class Question124(BaseQuestion):
    def __init__(self):
        self.type = [Types.Geometry_triangle, Types.sat_reasoning]
        self.complexity = Complexity.Moderate
        self.a = random.choice([20, 25, 30, 35, 40, 45, 50, 55, 60])
        self.b = random.choice([20, 25, 30, 35, 40, 45, 50, 55, 60])
        self.body = "In the given figure, how many cuboids are there?"

    def question(self):
        return self.body

    def answer(self):
        return "There are {0} cuboids".format(self.res)


    def graphic(self):
        # prepare some coordinates
        space = random.choice([5,6,7])
        x, y, z = np.indices((space, space, space))

        diffy = random.choice([2,3,4])
        diffx = random.choice([1,2,3,4])
        # draw cuboids in the top left and bottom right corners, and a link between them
        cube1 = (x < space-diffx) & (y < space) & (z < space)
        cube2 = (x < space) & (y < space-diffy) & (z < space)

        # combine the objects into a single boolean array
        voxels = cube1 | cube2
        self.res = np.sum(voxels)
        # set the colors of each object
        colors = np.empty(voxels.shape, dtype=object)
        colors[cube1] = 'white'
        colors[cube2] = 'white'

        plt.axis('equal')
        plt.gcf().set_size_inches(4, 4)

        # and plot everything
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.voxels(voxels, facecolors=colors, edgecolor='k')

        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )

