from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity
import random
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from io import BytesIO


class Question123(BaseQuestion):
    def __init__(self):
        self.type = [Types.Geometry_triangle, Types.sat_reasoning]
        self.complexity = Complexity.Moderate
        self.a = random.choice([20, 25, 30, 35, 40, 45, 50, 55, 60])
        self.b = random.choice([20, 25, 30, 35, 40, 45, 50, 55, 60])
        self.body = "In the given figure, what is the unknown angle?"

    def question(self):
        return self.body

    def answer(self):
        return "{0}\u00b0".format(180.0 - self.a -self.b)


    def graphic(self):
        plt.axis('equal')
        plt.gcf().set_size_inches(4, 4)
        #write down all the coordinates and write first one again, to form a closed loop,
        #separate the x's and y's into two lists as below.
        plt.plot([0, 1.7, 2, 0],[0, 2, 0, 1])
        r=2
        angle = max(30,self.a) # dont want to draw too narrow. limit to 30 degree
        rad=(angle*math.pi)/180.0
        plt.gca().add_patch(Arc([2,0], 0.2, 0.2, angle=200, theta1=255, theta2=310, color="blue"))
        plt.gca().add_patch(Arc([0.6,0.7], 0.2, 0.2, angle=300, theta1=220, theta2=290, color="blue"))
        plt.text(1.77,0.15,str(self.a)+u"\u00b0")
        plt.text(0.27,0.60,str(self.b)+u"\u00b0")
        plt.text(1.63,1.75,"?")
        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )

