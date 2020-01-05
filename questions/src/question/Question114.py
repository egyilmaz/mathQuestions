import random
from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity


class Question114(BaseQuestion):
    def __init__(self):
        self.type = [Types.Arithmetic, Types.sat_reasoning]
        self.complexity = Complexity.Moderate
        self.divisor = random.choice([8,9,11,12,13,14,15,16])
        self.quotient = random.choice([13,14,15,23,24,25])
        self.remainder = random.choice([1,2,3,4,5,6,7])
        self.dividend = self.divisor*self.quotient + self.remainder
        self.body = " "

    def question(self):
        return self.body

    def answer(self):
        return "Answer is {0} remainder {1} and ".format(self.quotient,self.remainder)

    def graphic(self):
        a = r"Find {0} $\div$ {1} = ?  remainder  ? . Write it in ${2}\dfrac{{{3}}}{{{4}}}$ form"\
            .format(self.dividend,self.divisor,'?','?','?')
        return self.encode_graphics(a)

    def answer_graphic(self):
        a = r"${0}\dfrac{{{1}}}{{{2}}}$".format(self.quotient,self.remainder,self.divisor)
        return self.encode_graphics(a)
