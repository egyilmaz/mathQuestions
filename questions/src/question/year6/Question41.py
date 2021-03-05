from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.resources.Resource import simple_fractions
from questions.src.question.utils.Utility import get_n_distinct
from questions.src.question.year6.Types import Types, Complexity


class Question41(BaseQuestion):
    def __init__(self):
        self.type = Types.Fraction_add
        self.complexity = Complexity.Advanced
        self.ratio3, self.ratio2, self.ratio1 = get_n_distinct(simple_fractions,3)

        self.res = self.ratio1 + self.ratio2 - self.ratio3

    def question(self):
        return "Calculate "

    def graphic(self):
        a = r'$\dfrac{{{0}}}{{{1}}}$ + $\dfrac{{{2}}}{{{3}}}$ - $\dfrac{{{4}}}{{{5}}}$'\
            .format(self.ratio1.numerator, self.ratio1.denominator,
                    self.ratio2.numerator, self.ratio2.denominator,
                    self.ratio3.numerator, self.ratio3.denominator,)
        return self.encode_graphics(a)

    def answer(self):
        return "Answer is "

    def answer_graphic(self):
        a = r'$\dfrac{{{0}}}{{{1}}}$'.format(self.res.numerator, self.res.denominator)
        return self.encode_graphics(a)

