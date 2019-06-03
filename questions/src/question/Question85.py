from .BaseQuestion import BaseQuestion
from fractions import Fraction
from .utils.Utility import get_two_distinct
from .Types import Types, Complexity


class Question85(BaseQuestion):
    def __init__(self):
        self.type = Types.Fraction_decimal
        self.complexity = Complexity.Basic
        self.pool = [0.1,0.2,0.3,0.5,0.6,0.7,1.0]
        self.first, self.second = get_two_distinct( self.pool )
        self.body = "Represent {0} and {1} as fractions.".format(self.first,self.second)
        self.res1,self.res2 = Fraction(int(self.first*10),10), Fraction(int(self.second*10),10)

    def question(self):
        return self.body

    def answer_graphic(self):
        a = r'$\dfrac{{{0}}}{{{1}}}$  and  $\dfrac{{{2}}}{{{3}}}$'.format(self.res1.numerator,self.res1.denominator,self.res2.numerator,self.res2.denominator)
        return self.encode_graphics(a)
