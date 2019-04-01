import random
from .BaseQuestion import BaseQuestion
from .Types import Types
from ..resources.Resource import simple_fractions
from ..utils.Utility import ask_interactive_1arg, get_n_distinct

def cube(num):
    return num*num*num

class Question24(BaseQuestion):
    def __init__(self):
        self.type = Types.FIRST_ORDER_1_UNKNOWN
        self.first, self.second, self.third, self.fourth = get_n_distinct(range(0,11),4)
        self.res = [cube(self.first),cube(self.second),cube(self.third),cube(self.fourth)]

    def question(self):
        return "Calculate   "

    def graphic(self):
        a = r'${0}^3, {1}^3, {2}^3, {3}^3$'.format(self.first,self.second,self.third,self.fourth)
        return self.encode_graphics(a)

    def ask_user(self):
        return self.res == ask_interactive_1arg(self.question())

    def result(self):
        return {self.res: self.res}

    def answer(self):
        return "{res}".format(res=self.res)