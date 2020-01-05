import random
from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity


class Question113(BaseQuestion):
    def __init__(self):
        self.type = [Types.Geometry_circle_perimeter, Types.sat_reasoning]
        self.complexity = Complexity.Moderate
        diameter = random.choice([40, 50, 90, 100])
        self.body = "A car tyre is {0} diameter. what is the area and perimeter of this tyre(Take pi as 3.14)"\
            .format(diameter)
        perimeter = 3.14*diameter
        area = 3.14*(diameter/2)**2
        self.res="perimeter is 2*pi*r = {0} and area is pi*r^2 = {1}".format(perimeter, area)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
