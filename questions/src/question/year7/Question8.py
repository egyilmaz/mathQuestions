from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.resources.Resource import random_fractions
from questions.src.question.utils.Utility import get_unsorted_n_distinct
from questions.src.question.year7.Types import Types, Complexity
from fractions import Fraction
import random


class Question8(BaseQuestion):
    def __init__(self):
        self.type = Types.fraction_unknown
        self.complexity = Complexity.Basic
        ratio1, ratio2 = get_unsorted_n_distinct(random_fractions,2)
        c1, c2 = random.sample([2,3,4,5,6],2)
        res = ratio1 + ratio2
        res = - Fraction(res.numerator*c2, res.denominator*c1)

        self.q = r'$\dfrac{{{0}}}{{{1}}}$ + $\dfrac{{{2}}}{{{3}}}$ + $\dfrac{{{4}X}}{{{5}}} $ = 0, What is X' \
            .format(ratio1.numerator, ratio1.denominator,
                    ratio2.numerator, ratio2.denominator,
                    c1, c2)

        self.a = r'$\dfrac{{{0}}}{{{1}}}$'.format(res.numerator, res.denominator)

    def question(self):
        return "Given, "

    def graphic(self):
        return self.encode_graphics(self.q)

    def answer_graphic(self):
        return self.encode_graphics(self.a)