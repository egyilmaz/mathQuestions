import random
from .BaseQuestion import BaseQuestion
from .resources.Resource import boys, items, random_fractions
from .utils.Utility import get_two_distinct
from .Types import Types, Complexity


class Question38(BaseQuestion):
    def __init__(self):
        self.type = Types.Equation_First_order_one_unknown
        self.complexity = Complexity.Moderate
        self.coeff=random.choice([2,3,4,5,6,7,8,9,10,11,12])
        self.const=random.choice([10,20,30,40,50,60,70,80])
        self.res = random.choice([4,5,6,7,8])
        self.get = self.res*self.coeff + self.const
        self.body = "If we multiply a number with {coeff} and then add {const} to it. we get {get}. What is that number?"\
            .format(coeff=self.coeff, const=self.const, get=self.get)

    def question(self):
        return self.body

    def answer(self):
        return "That number is {res}".format(res=self.res)
