from .BaseQuestion import BaseQuestion
from .resources.Resource import simple_fractions
from .utils.Utility import get_two_distinct
from .Types import Types, Complexity


class Question17(BaseQuestion):
    def __init__(self):
        self.type = Types.Fraction_compare
        self.complexity = Complexity.Basic
        self.ratio1, self.ratio2 = get_two_distinct(simple_fractions)
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
