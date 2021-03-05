import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year6.Types import Types, Complexity


class Question132(BaseQuestion):
    def __init__(self):
        self.type = [Types.Geometry_line, Types.sat_reasoning]
        self.complexity = Complexity.Moderate
        line = random.choice([6,7,8,9,10,11,12])
        factor = random.choice([3,4,5,6,7,8])
        self.body = "What will be the new length of a {0}cm line when it is enlarged by a scale factor of {1}"\
            .format(line, factor)

        self.res="{0}".format(line*factor)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
