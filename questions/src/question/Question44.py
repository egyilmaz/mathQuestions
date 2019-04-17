import random
from .BaseQuestion import BaseQuestion
from .resources.Resource import boys, items, random_fractions
from .utils.Utility import get_two_distinct
from .Types import Types, Complexity


class Question44(BaseQuestion):
    def __init__(self):
        self.type = Types.Conversion
        self.complexity = Complexity.Advanced
        self.moderate = random.choice([2.1,3.2,3.4,3.6])
        self.advanced = random.choice([10,20,123, 980])
        self.body = "Convert {mod} liter to millileter, {adv}millileter to liter".format(mod=self.moderate,adv=self.advanced)
        self.res="{0}ml {1}L".format(self.moderate*1000.0,self.advanced/1000.0)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
