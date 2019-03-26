import random
from .BaseQuestion import BaseQuestion
from .Types import Types
from ..resources.Resource import simple_fractions
from ..utils.Utility import ask_interactive_1arg, get_two_distinct


class Question17(BaseQuestion):
    def __init__(self):
        self.type = Types.FIRST_ORDER_1_UNKNOWN
        self.ratio1, self.ratio2 = get_two_distinct(simple_fractions)
        self.res = (self.ratio1 - self.ratio2 ) > 0
        self.body = "{ratio1} > {ratio2}  Is this the correct ordering?".format(ratio1=self.ratio1, ratio2=self.ratio2)

    def question(self):
        return self.body

    def ask_user(self):
        return self.res == ask_interactive_1arg(self.question())

    def result(self):
        return {self.res: self.res}

    def answer(self):
        return "{res}".format(res=self.res)

