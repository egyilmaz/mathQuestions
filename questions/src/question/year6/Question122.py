from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year6.Types import Types, Complexity
import random
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from io import BytesIO


class Question122(BaseQuestion):
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
        plt.plot([1, 2, 1.5, 1],[1, 1, 1.5, 1])
        r=2
        angle = max(30,self.a) # dont want to draw too narrow. limit to 30 degree
        rad=(angle*math.pi)/180.0
        plt.gca().add_patch(Arc([2,1], 0.2, 0.2, angle=240, theta1=255, theta2=300, color="blue"))
        plt.gca().add_patch(Arc([1,1], 0.2, 0.2, angle=0, theta1=0, theta2=45, color="blue"))
        plt.text(1.8,1.05,str(self.a)+u"\u00b0")
        plt.text(1.1,1.04,str(self.b)+u"\u00b0")
        plt.text(1.5,1.4,"?")
        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )

