from .BaseQuestion import BaseQuestion
from .resources.Resource import simple_fractions
from .utils.Utility import get_n_distinct
from .Types import Types, Complexity


class Question41(BaseQuestion):
    def __init__(self):
        self.type = Types.Fraction_add
        self.complexity = Complexity.Advanced
        self.ratio1, self.ratio2, self.ratio3 = get_n_distinct(simple_fractions,3)
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
        return "{res}".format(res=self.res)
