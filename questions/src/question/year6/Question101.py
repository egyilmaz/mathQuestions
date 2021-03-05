import random
from fractions import Fraction
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.Types import Types, Complexity


class Question101(BaseQuestion):
    def __init__(self):
        self.type = [Types.Fraction_add, Types.sat_arithmetic]
        self.complexity = Complexity.Moderate
        self.ratio1 = random.choice([Fraction(12,7), Fraction(16,5), Fraction(30,14), Fraction(20,3), Fraction(12,5)])
        self.divisor = random.choice([1, 2, 3, 4, 5])
        self.res = self.ratio1 / self.divisor


    def question(self):
        return "Calculate "

    def graphic(self):
        a = r'$\dfrac{{{0}}}{{{1}}} \div {2}$ = ?'\
            .format(self.ratio1.numerator, self.ratio1.denominator, self.divisor)
        return self.encode_graphics(a)

    def answer(self):
        return "Answer is"

    def answer_graphic(self):
        a = r'$\dfrac{{{0}}}{{{1}}}$'.format(self.res.numerator, self.res.denominator)
        return self.encode_graphics(a)
