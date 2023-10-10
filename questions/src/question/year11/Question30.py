from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_unsorted_n_distinct, get_two_distinct
from questions.src.question.year11.Types import Types, Complexity
import sympy as sp
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from io import BytesIO
from .utils import cartesian, draw_rectangle, draw_triangle

class Question30(BaseQuestion):
    def __init__(self):
        self.type = [Types.translate_rotate]
        self.complexity = Complexity.Complex
        r = random.sample([2, 3, 4, 5],1)[0]
        self.rad = r
        self.sol = ((2*r**2) - ((sp.pi*r**2)/4 + (r**2)/2))

    def question(self):
        return ""

    def answer(self):
        return f"Gray area is {sp.nsimplify(self.sol)}"

    def graphic(self):
        #plt.rcParams['text.usetex'] = True
        # Create a figure and axis
        radius = self.rad
        xmin, xmax, ymin, ymax = 0, radius*2+1, 0, radius
        fig, ax = cartesian(xmin, xmax, ymin, ymax)

        ax.add_patch(patches.Rectangle((0,0), radius*2, radius, color='gray'))
        # Define the center and radius of the quarter circle
        circle_center = (0, 0)
        ax.add_patch(patches.Wedge(circle_center, radius, 0, 90, fill=True))

        x = [radius, radius*2, radius*2]
        y = [0, radius, 0]
        ax.add_patch(patches.Polygon([(radius,0),(radius*2,radius),(radius*2,0)], closed=True))
        ax.set_title(r'Find the gray area, leave $\pi$ as is', fontsize=16)
        # Display the plot
        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )
