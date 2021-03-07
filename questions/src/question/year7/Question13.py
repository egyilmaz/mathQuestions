from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.resources.Resource import simple_fractions
from questions.src.question.utils.Utility import get_unsorted_n_distinct
from questions.src.question.year7.Types import Types, Complexity


class Question13(BaseQuestion):
    def __init__(self):
        self.type = Types.fraction_equation
        self.complexity = Complexity.Basic
        ratio1, ratio2, ratio3 = get_unsorted_n_distinct(simple_fractions,3)
        res = -ratio2 / (ratio1 - ratio3)
        self.q = r'$\dfrac{{{0}X}}{{{1}}} + \dfrac{{{2}}}{{{3}}} = \dfrac{{{4}X}}{{{5}}}$, What is X' \
            .format(ratio1.numerator, ratio1.denominator,
                    ratio2.numerator, ratio2.denominator,
                    ratio3.numerator, ratio3.denominator,
                    )

        self.a = r'$\dfrac{{{0}}}{{{1}}}$'.format(res.numerator, res.denominator)

    def question(self):
        return "Given, "

    def graphic(self):
        return self.encode_graphics(self.q)

    def answer_graphic(self):
        return self.encode_graphics(self.a)