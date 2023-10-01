from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_unsorted_n_distinct, get_two_distinct
from questions.src.question.year11.Types import Types, Complexity
from itertools import chain
import numpy as np
import random
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from io import BytesIO
from .utils import cartesian, rotate, draw_triangle

class Question26(BaseQuestion):
    def __init__(self):
        self.type = [Types.translate_rotate]
        self.complexity = Complexity.Moderate
        self.x = [1, 4, 2]
        self.y = [2, 4, 4]
        self.ang = random.choice([90, 180, 270])
        self.r_x,self.r_y = random.choice([(0,0)])
        tri_ang = [(self.x[i],self.y[i]) for i in range(3)]
        self.body = f"Given a triangle with points on {tri_ang}, what must be the rotation angle around origin to draw the second triangle"

    def question(self):
        return self.body

    def answer(self):
        return f"rotation angle around origin must be {self.ang}"

    def graphic(self):
        xmin, xmax, ymin, ymax = -5, 5, -5, 5
        fig, ax = cartesian(xmin, xmax, ymin, ymax)
        draw_triangle(self.x, self.y)
        # Show the plot
        plt.grid(True)        
       
        new_vertices = rotate(self.x,self.y, self.ang, (self.r_x,self.r_y))
        # Extract the new x and y coordinates
        new_x, new_y = new_vertices
        plt.plot(new_x.tolist() + [new_x[0]], new_y.tolist() + [new_y[0]], marker='o', linestyle='-')

        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )
