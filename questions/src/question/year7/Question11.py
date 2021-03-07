from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.resources.Resource import random_fractions
from questions.src.question.utils.Utility import get_unsorted_n_distinct
from questions.src.question.year7.Types import Types, Complexity
from fractions import Fraction
import random


class Question11(BaseQuestion):
    def __init__(self):
        self.type = Types.fraction_to_whole
        self.complexity = Complexity.Basic
        r = random.choice(random_fractions)
        c = random.choice([6,7,8,9,10,11,12,13,14,15])

        self.q = r'What will be the whole if $\dfrac{{{0}}}{{{1}}}$ = {2}'.format(r.numerator, r.denominator,c)
        res = Fraction(c*r.denominator, r.numerator)
        self.a = r'$\dfrac{{{0}}}{{{1}}}$'.format(res.numerator, res.denominator)

    def question(self):
        return ""

    def graphic(self):
        return self.encode_graphics(self.q)

    def answer_graphic(self):
        return self.encode_graphics(self.a)