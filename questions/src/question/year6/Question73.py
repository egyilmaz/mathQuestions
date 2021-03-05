from questions.src.question.BaseQuestion import BaseQuestion
from fractions import Fraction
from questions.src.question.utils.Utility import get_two_distinct
from questions.src.question.year6.Types import Types, Complexity


class Question73(BaseQuestion):
    def __init__(self):
        self.type = Types.Fraction_decimal
        self.complexity = Complexity.Moderate
        self.pool = [Fraction(1,4),Fraction(3,4), Fraction(3,20),Fraction(1,25),Fraction(49,50),Fraction(23,25),Fraction(4,5)]
        self.first, self.second = get_two_distinct( self.pool )
        self.res = "{0}, {1}".format(float(self.first), float(self.second))
        self.body = "Represent  "

    def question(self):
        return self.body

    def graphic(self):
        a = r'$\dfrac{{{0}}}{{{1}}}$  and  $\dfrac{{{2}}}{{{3}}}$ as decimals'.format(self.first.numerator,self.first.denominator,self.second.numerator,self.second.denominator)
        return self.encode_graphics(a)

    def answer(self):
        return "{res}".format(res=self.res)
