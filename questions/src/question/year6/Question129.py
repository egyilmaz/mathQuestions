import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year6.Types import Types, Complexity


def factors(x):
    return [i for i in range(1,x+1) if x%i==0]


class Question129(BaseQuestion):
    def __init__(self):
        self.type = [Types.Factors, Types.sat_reasoning]
        self.complexity = Complexity.Moderate
        number = random.choice([12, 15, 24, 28, 36])
        self.body = "Find the factors of {0}".format(number)
        self.res="{0}".format(factors(number))

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
