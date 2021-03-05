from questions.src.question.BaseQuestion import BaseQuestion
from fractions import Fraction
from questions.src.question.utils.Utility import get_two_distinct
from questions.src.question.Types import Types, Complexity

class Question28(BaseQuestion):
    def __init__(self):
        self.type = [Types.Percentage,Types.sat_arithmetic]
        self.complexity = Complexity.Moderate
        self.first, self.second = get_two_distinct([2,5,10,20,25,30,40,50,60,75,90,100])
        self.res1 = Fraction(self.first,100)
        self.res2 = Fraction(self.second,100)
        self.body = "Represent {0}% and {1}% as fractions".format(self.first, self.second)

    def question(self):
        return self.body

    def answer(self):
        return "Answer is "

    def answer_graphic(self):
        a = r'$\dfrac{{{0}}}{{{1}}}$  and  $\dfrac{{{2}}}{{{3}}}$'.format(self.res1.numerator,self.res1.denominator
                                                                          ,self.res2.numerator,self.res2.denominator)
        return self.encode_graphics(a)
