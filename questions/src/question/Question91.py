from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity
import random
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from io import BytesIO


class Question91(BaseQuestion):
    def __init__(self):
        self.type = Types.Chart
        self.complexity = Complexity.Basic
        self.angle = random.choice([20, 25, 30, 35, 40, 45, 50, 55, 60, 70, 80])
        self.body = "In the given figure, what is the complementing angle?".format(self.angle)

    def question(self):
        return self.body

    def answer(self):
        return "{0}\u00b0".format(180.0 - self.angle)

    def graphic(self):
        plt.axis('equal')
        plt.gcf().set_size_inches(4, 4)
        plt.plot([-2,2], [0, 0],color="black")
        r=2
        angle = max(30,self.angle) # dont want to draw too narrow. limit to 30 degree
        rad=(angle*math.pi)/180.0
        plt.gca().add_patch(Arc([0,0], 0.5, 0.5, 0, 0, angle,color="blue"))
        plt.text(0.4,0.05,str(self.angle)+u"\u00b0")
        plt.plot([0,r*math.cos(rad)],[0,r*math.sin(rad)])
        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )

