import random
from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity


class Question133(BaseQuestion):
    def __init__(self):
        self.type = [Types.Geometry_square_area, Types.sat_reasoning]
        self.complexity = Complexity.Moderate
        side = random.choice([3,4,5])
        factor = random.choice([2,3,4,5])
        self.body = "What will be the new area of a square with a side of {0}cm is enlarged on all sides equally " \
                    "by a scale factor of {1}".format(side,factor)

        self.res="{0}".format(side*factor*side*factor)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
