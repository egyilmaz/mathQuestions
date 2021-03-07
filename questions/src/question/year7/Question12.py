from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.resources.Resource import random_fractions
from questions.src.question.utils.Utility import get_unsorted_n_distinct
from questions.src.question.year7.Types import Types, Complexity
from fractions import Fraction
import random


class Question12(BaseQuestion):
    def __init__(self):
        self.type = Types.fraction_equation
        self.complexity = Complexity.Basic
        ratio1, ratio2 = get_unsorted_n_distinct(random_fractions,2)
        res = Fraction(ratio1.numerator*ratio2.denominator, ratio1.denominator*ratio2.numerator)

        self.q = r'$\dfrac{{{0}}}{{{1}}} = \dfrac{{{2}X}}{{{3}}}    $, What is X' \
            .format(ratio1.numerator, ratio1.denominator,
                    ratio2.numerator, ratio2.denominator)

        self.a = r'$\dfrac{{{0}}}{{{1}}}$'.format(res.numerator, res.denominator)

    def question(self):
        return "Given, "

    def graphic(self):
        return self.encode_graphics(self.q)

    def answer_graphic(self):
        return self.encode_graphics(self.a)