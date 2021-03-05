from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.resources.Resource import random_fractions
from questions.src.question.utils.Utility import get_unsorted_n_distinct
from questions.src.question.year6.Types import Types, Complexity


class Question76(BaseQuestion):
    def __init__(self):
        self.type = Types.Fraction_compare
        self.complexity = Complexity.Moderate
        self.ratio1, self.ratio2 = get_unsorted_n_distinct(random_fractions,2)
        self.res = (self.ratio1 - self.ratio2 ) > 0

    def question(self):
        return "Is the given orderding correct? "

    def graphic(self):
        a = r'$\dfrac{{{0}}}{{{1}}}$ > $\dfrac{{{2}}}{{{3}}}$ = ?' \
            .format(self.ratio1.numerator, self.ratio1.denominator,
                    self.ratio2.numerator, self.ratio2.denominator)
        return self.encode_graphics(a)

    def answer(self):
        return "Answer is "+str(self.res)
