import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.resources.Resource import boys, simple_fractions
from questions.src.question.utils.Utility import get_two_distinct
from questions.src.question.year6.Types import Types, Complexity


class Question16(BaseQuestion):
    def __init__(self):
        self.type = [Types.Fraction_add, Types.sat_arithmetic]
        self.complexity = Complexity.Basic
        self.subject = random.choice(boys)
        self.ratio1, self.ratio2 = get_two_distinct(simple_fractions)
        self.res = self.ratio1 + self.ratio2


    def question(self):
        return "Calculate "

    def graphic(self):
        a = r'$\dfrac{{{0}}}{{{1}}}$ + $\dfrac{{{2}}}{{{3}}}$ = ?'\
            .format(self.ratio1.numerator, self.ratio1.denominator,
                    self.ratio2.numerator, self.ratio2.denominator)
        return self.encode_graphics(a)

    def answer(self):
        return "Answer is"

    def answer_graphic(self):
        a = r'$\dfrac{{{0}}}{{{1}}}$'.format(self.res.numerator, self.res.denominator)
        return self.encode_graphics(a)
