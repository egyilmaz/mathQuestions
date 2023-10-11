from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_unsorted_n_distinct, get_two_distinct
from questions.src.question.year11.Types import Types, Complexity
import math
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from io import BytesIO
from .utils import cartesian, draw_rectangle, draw_triangle

class Question31(BaseQuestion):
    def __init__(self):
        self.type = [Types.trigonometry]
        self.complexity = Complexity.Basic
        self.ang = random.sample([30, 45, 60],1)[0]
        self.hyp = random.sample([10, 20, 30, 40, 50],1)[0]
        self.sol = round(self.hyp*math.sin(math.pi*self.ang/180),2)

    def question(self):
        return ""

    def answer(self):
        return f"x is {self.sol}"

    def graphic(self):
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.set_aspect('equal')

        # Set axis limits
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)

        # Display the plot
        plt.axis('off')        
        ax.add_patch(patches.Polygon([(0,0),(5,0),(5,8)], closed=True))

        # Define the center and radius of the quarter circle
        circle_center = (0, 0)
        ax.add_patch(patches.Wedge(circle_center, 0.5, 0, 56, color='red',fill=True))
        ax.text(0.6, 0.2, f'${self.ang}^o$')

        rectangle = plt.Rectangle((4.48, 0), 0.5, 0.5, fill=True, color='red')
        ax.add_patch(rectangle)

        ax.text(1.4, 3.5, f"{self.hyp}cm", rotation=55)
        ax.text(5.3, 3.8, "x = ?")

        # Display the plot
        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )
