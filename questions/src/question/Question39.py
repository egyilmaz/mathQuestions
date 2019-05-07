import random
from .BaseQuestion import BaseQuestion
from .resources.Resource import random_fractions
from .utils.Utility import get_two_distinct
from .Types import Types, Complexity


class Question39(BaseQuestion):
    def __init__(self):
        self.type = Types.Equation_First_order_one_unknown
        self.complexity = Complexity.Advanced
        self.ratio1, self.ratio2 = get_two_distinct(random_fractions)
        self.res = random.choice(range(2,10))*self.ratio1.denominator*self.ratio2.denominator
        self.got = self.res*self.ratio1 + self.res*self.ratio2

    def question(self):
        return " "

    def graphic(self):
        a = r'When we add $\dfrac{{{0}}}{{{1}}}$ of a number to $\dfrac{{{2}}}{{{3}}}$ of the same number we get {4}. What is that number'\
            .format(self.ratio1.numerator, self.ratio1.denominator, self.ratio2.numerator, self.ratio2.denominator, self.got)
        return self.encode_graphics(a)

    def answer(self):
        return "{res}".format(res=self.res)
