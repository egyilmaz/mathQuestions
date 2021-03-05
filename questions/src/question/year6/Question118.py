import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year6.Types import Types, Complexity


class Question118(BaseQuestion):
    def __init__(self):
        self.type = [Types.Problem_solving, Types.sat_reasoning]
        self.complexity = Complexity.Moderate
        points = random.choice([6, 7, 8, 9])
        segment = random.choice([50, 60, 70, 80])
        self.body = "On a map, two cities are joined with {0} equaly spaced dots that form a straight line. If the " \
                    "distance between these two cities are {1}, what is the lenght of each segment between two dots " \
                    "and what will be the distance between 2nd and 2nd from last point?"\
            .format(points, segment*(points-1))
        self.res = "Each segment is {0}, Distance between 2nd and 2nd from last point is {1}"\
            .format(segment, segment*(points-3))

    def question(self):
        return self.body

    def answer(self):
        return self.res
