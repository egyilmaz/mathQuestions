from questions.src.question.BaseQuestion import BaseQuestion
from fractions import Fraction
from questions.src.question.utils.Utility import get_two_distinct
from questions.src.question.year6.Types import Types, Complexity


class Question72(BaseQuestion):
    def __init__(self):
        self.type = Types.Fraction_decimal
        self.complexity = Complexity.Basic
        self.pool = [Fraction(1,2),Fraction(2,2),Fraction(3,5), Fraction(4,5),Fraction(1,10),Fraction(9,10),Fraction(3,100),Fraction(13,100),Fraction(37,100),Fraction(51,100)]
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
