import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.Types import Types, Complexity


class Question130(BaseQuestion):
    def __init__(self):
        self.type = [Types.Decimal, Types.sat_reasoning]
        self.complexity = Complexity.Moderate
        first_grp = random.sample([0.01,0.1,0.001,0.0001],2)
        second_grp = random.sample([10,100,1000,10000],2)
        first = random.choice(first_grp)
        second = random.choice(second_grp)
        result = round(first*second,6)
        self.body = "Which two of the {0} multiplies to {1}".format(first_grp+second_grp, result)

        self.res="{0} and {1}".format(first, second)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
