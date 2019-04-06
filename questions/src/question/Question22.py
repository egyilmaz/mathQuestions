import random
from .BaseQuestion import BaseQuestion
from .Types import Types
from ..resources.Resource import boys, items, simple_fractions
from ..utils.Utility import ask_interactive_1arg, get_two_distinct


class Question22(BaseQuestion):
    def __init__(self):
        self.type = Types.FIRST_ORDER_1_UNKNOWN
        self.subject = random.choice(boys)
        self.ratio1, self.ratio2 = get_two_distinct(simple_fractions)
        self.int1, self.int2 = get_two_distinct(range(1,7))
        self.res = str(self.int1+self.int2)+"+"+str(self.ratio1 + self.ratio2)

    def question(self):
        return "Calculate   "

    def graphic(self):
        a = r'${0} \dfrac{{{1}}}{{{2}}} + {3}\dfrac{{{4}}}{{{5}}}$'.format(self.int1,self.ratio1.numerator,self.ratio1.denominator,self.int2,self.ratio2.numerator,self.ratio2.denominator)
        return self.encode_graphics(a)

    def ask_user(self):
        return self.res == ask_interactive_1arg(self.question())

    def result(self):
        return {self.subject: self.res}

    def answer(self):
        return "Result is {res}".format(res=self.res)
