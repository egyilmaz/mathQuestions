import random
from .BaseQuestion import BaseQuestion
from .resources.Resource import boys, simple_fractions
from .utils.Utility import get_two_distinct
from .Types import Types, Complexity

class Question22(BaseQuestion):
    def __init__(self):
        self.type = Types.Fraction_add
        self.complexity = Complexity.Moderate
        self.subject = random.choice(boys)
        self.ratio1, self.ratio2 = get_two_distinct(simple_fractions)
        self.int1, self.int2 = get_two_distinct(range(1,7))
        self.res = str(self.int1+self.int2)+"+"+str(self.ratio1 + self.ratio2)

    def question(self):
        return "Calculate   "

    def graphic(self):
        a = r'${0} \dfrac{{{1}}}{{{2}}} + {3}\dfrac{{{4}}}{{{5}}}$'.format(self.int1,self.ratio1.numerator,self.ratio1.denominator,self.int2,self.ratio2.numerator,self.ratio2.denominator)
        return self.encode_graphics(a)

    def answer(self):
        return "Result is {res}".format(res=self.res)
