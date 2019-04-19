import random
import matplotlib.pyplot as plt
from .utils.Utility import get_two_distinct
from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity
from django.template import Template

class Question54(BaseQuestion):
    def __init__(self):
        self.type = Types.Geometry_circle_perimeter
        self.complexity = Complexity.Moderate
        self.coef1,self.coef2 = get_two_distinct([2,3,4,5])
        self.var1 = random.choice(['x','y','z'])
        self.num1 = random.choice([2,3,4,5])
        self.asked = self.coef1*self.num1*self.num1 + self.coef2*self.num1*self.num1

    def question(self):
        return "Given the circle with radius 5inch below, What is the perimeter? (P = 2*pi*radius, where pi is 3.0)"

    def graphic(self):
        circle = plt.Circle((0.5, 0.5), radius=0.5, fc='y')
        plt.gcf().set_size_inches(1,1)
        return self.draw_shape( circle )

    def answer(self):
        return "{res}".format(res=self.num1)

    def template(self):
        return Template("{{ text }}<br><div class=\"qi\"><img src=\"data:image/png;base64,{{graphic}}\"></div>")