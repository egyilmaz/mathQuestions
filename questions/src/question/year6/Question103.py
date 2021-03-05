import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.Types import Types, Complexity


class Question103(BaseQuestion):
    def __init__(self):
        self.type = [Types.Arithmetic,Types.sat_arithmetic]
        self.complexity = Complexity.Basic
        self.first = random.choice([16, 25, 32, 41, 17, 23, 28, 34])
        self.second = random.choice([8, 9, 10, 11, 12, 14, 15, 20, 30, 40])
        self.third = random.choice(range(2,10))
        self.fourth = random.choice(range(2,10))
        self.body = "{3} + ({0} - {2}) x {1}= ".format(self.first, self.second, self.third, self.fourth)
        self.res="{0}".format((self.first-self.third)*self.second+self.fourth)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
