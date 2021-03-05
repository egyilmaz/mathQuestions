from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.resources.Resource import random_fractions
from questions.src.question.utils.Utility import get_two_distinct, descending
from questions.src.question.Types import Types, Complexity

class Question25(BaseQuestion):
    def __init__(self):
        self.type = [Types.Fraction_sub, Types.sat_arithmetic]
        self.complexity = Complexity.Basic
        self.first, self.second = descending( *get_two_distinct( random_fractions ) )
        self.res = self.first - self.second
        self.body = "Calculate   "

    def question(self):
        return self.body

    def graphic(self):
        a = r'$\dfrac{{{0}}}{{{1}}}  -  \dfrac{{{2}}}{{{3}}}$'.format(self.first.numerator,self.first.denominator,self.second.numerator,self.second.denominator)
        return self.encode_graphics(a)

    def answer(self):
        return "Answer is "

    def answer_graphic(self):
        a = r'$\dfrac{{{0}}}{{{1}}}$'.format(self.res.numerator, self.res.denominator)
        return self.encode_graphics(a)
