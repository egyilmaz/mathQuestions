import random
from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity
from .resources.Resource import subjects


class Question134(BaseQuestion):
    def __init__(self):
        self.type = [Types.General_Problem, Types.sat_reasoning]
        self.complexity = Complexity.Moderate
        actor = random.choice(subjects)
        prop = random.choice(["hat","pen","coat","shoe","jean"])
        price = random.choice([10,15,20,25,30])
        discount = random.choice([10,15,20,25])
        self.body = "{0} fancies buying a {1} that costs {2} pounds, how much will it cost after applying a end-of-season" \
                    " discount of {3}% ".format(actor,prop,price,discount)

        self.res="{0}".format(round(price - price*discount/100,2))

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
