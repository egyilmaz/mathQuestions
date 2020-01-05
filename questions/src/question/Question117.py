import random
from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity


class Question117(BaseQuestion):
    def __init__(self):
        self.type = [Types.Estimation, Types.sat_reasoning]
        self.complexity = Complexity.Moderate
        time = random.choice([6.8, 7.9, 9.9, 3.1, 2.9, 4.2, 4.1])
        amount = random.choice([11, 19, 21, 28, 29, 40, 30, 41])
        self.body = "A car factory can produce a car in {0} every hour, Estimate the amount of time" \
                    "it will take to produce of {1} cars?".format(time, amount)
        result = round(time) * round(amount, -1)
        self.res = "Answer is {0}".format(result)

    def question(self):
        return self.body

    def answer(self):
        return self.res
