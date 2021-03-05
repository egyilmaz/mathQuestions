from questions.src.question.BaseQuestion import BaseQuestion
from fractions import Fraction
from questions.src.question.utils.Utility import get_two_distinct
from questions.src.question.Types import Types, Complexity


class Question87(BaseQuestion):
    def __init__(self):
        self.type = Types.Fraction_decimal
        self.complexity = Complexity.Advanced
        self.pool = [0.001,0.123,0.301,0.005,1.001,1.002,12.123,123.456]
        self.first, self.second = get_two_distinct( self.pool )
        self.body = "Represent {0} and {1} as fractions.".format(self.first,self.second)
        self.res1,self.res2 = Fraction(int(self.first*100),100), Fraction(int(self.second*100),100)

    def question(self):
        return self.body

    def answer_graphic(self):
        a = r'$\dfrac{{{0}}}{{{1}}}$  and  $\dfrac{{{2}}}{{{3}}}$'.format(self.res1.numerator,self.res1.denominator,self.res2.numerator,self.res2.denominator)
        return self.encode_graphics(a)
