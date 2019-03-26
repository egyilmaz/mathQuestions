import random
from .BaseQuestion import BaseQuestion
from .Types import Types
from ..resources.Resource import simple_fractions
from ..utils.Utility import ask_interactive_1arg, get_n_distinct


class Question23(BaseQuestion):
    def __init__(self):
        self.type = Types.FIRST_ORDER_1_UNKNOWN
        self.base = get_n_distinct(range(1,11),1)[0]
        self.res = self.base * self.base

    def question(self):
        return "Calculate   "

    def graphic(self):
        a = r'${0}^2$'.format(self.base)
        return self.encode_graphics(a)

    def ask_user(self):
        return self.res == ask_interactive_1arg(self.question())

    def result(self):
        return {self.res: self.res}

    def answer(self):
        return "{res}".format(res=self.res)
