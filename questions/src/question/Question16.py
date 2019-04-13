import random
from .BaseQuestion import BaseQuestion
from .resources.Resource import boys, simple_fractions
from .utils.Utility import get_two_distinct


class Question16(BaseQuestion):
    def __init__(self):
        self.subject = random.choice(boys)
        self.ratio1, self.ratio2 = get_two_distinct(simple_fractions)
        self.res = self.ratio1 + self.ratio2
        self.body = "{ratio1} + {ratio2} = ?".format(ratio1=self.ratio1, ratio2=self.ratio2)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
