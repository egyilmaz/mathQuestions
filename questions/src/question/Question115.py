import random
from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity


class Question115(BaseQuestion):
    def __init__(self):
        self.type = [Types.Geometry_rectangle_area, Types.sat_reasoning]
        self.complexity = Complexity.Moderate
        one_side = random.choice([6,7,8,9,11,12,13,14])
        result = random.choice([12,13,14,15,16,17,18,19])
        self.body = "The area of a rectangle is {0}. If one side is {1}, what is the other side?"\
            .format(one_side*result,one_side)

        self.res = "Answer is {0}".format(result)

    def question(self):
        return self.body

    def answer(self):
        return self.res
