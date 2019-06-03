from .BaseQuestion import BaseQuestion
from fractions import Fraction
from .utils.Utility import get_two_distinct
from .Types import Types, Complexity


class Question86(BaseQuestion):
    def __init__(self):
        self.type = Types.Fraction_decimal
        self.complexity = Complexity.Moderate
        self.pool = [0.01,0.02,0.03,0.05,0.16,0.17,1.01, 2.12, 3.14, 5.05]
        self.first, self.second = get_two_distinct( self.pool )
        self.body = "Represent {0} and {1} as fractions.".format(self.first,self.second)
        self.res1,self.res2 = Fraction(int(self.first*100),100), Fraction(int(self.second*100),100)

    def question(self):
        return self.body

    def answer_graphic(self):
        a = r'$\dfrac{{{0}}}{{{1}}}$  and  $\dfrac{{{2}}}{{{3}}}$'.format(self.res1.numerator,self.res1.denominator,self.res2.numerator,self.res2.denominator)
        return self.encode_graphics(a)
