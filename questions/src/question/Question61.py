import random
from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity
from .resources.Resource import boys


class Question61(BaseQuestion):
    def __init__(self):
        self.type = [Types.Percentage, Types.sat_reasoning]
        self.complexity = Complexity.Moderate
        self.subj = random.choice(boys)
        self.tip = random.choice([5,10,15])
        self.bill = random.choice([100,200,300])
        self.body = "{subj} and his extended family ate at a restaurant and got a bill of {bill}pounds. If the tip is {tip}%,"\
                " What will be the total amount to pay?".format(subj=self.subj, bill = self.bill, tip=self.tip)
        self.res = self.bill * (1+self.tip/100.0)

    def question(self):
        return self.body

    def answer(self):
        return "Total bill comes to {0}".format(self.res)
