import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.Types import Types, Complexity


class Question104(BaseQuestion):
    def __init__(self):
        self.type = [Types.Arithmetic,Types.sat_arithmetic]
        self.complexity = Complexity.Basic
        self.first = random.choice([0.008, 0.9, 0.07, 0.12, 0.3, 2.3, 1.9, 1.09])
        self.second = random.choice([10, 100, 1000])
        self.third = random.choice(range(2,9))
        self.fourth = random.choice([10, 100, 1000])
        self.body = "{0} x {1} and {0} x {2} and {0} / {3} = ".format(self.first, self.second, self.third, self.fourth)
        self.res="{0} and {1} and {2}".format(self.first*self.second, self.first*self.third, self.first/self.fourth)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
