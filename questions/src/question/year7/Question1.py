from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_unsorted_n_distinct, get_two_distinct
from questions.src.question.year7.Types import Types, Complexity
from itertools import chain

def add_plus_sign(arr):
    res=[arr[0]]
    for i in arr[1:]:
        res.append(str(i) if i < 0 else f"+{i}")
    return res

class Question1(BaseQuestion):

    coeff = [i for i in chain(range(-11, -2), range(2, 11))]

    def __init__(self):
        self.type = Types.Simplfy_expression
        self.complexity = Complexity.Basic
        self.var1, self.var2 = get_two_distinct(['x', 'y', 'z', 't', 'a', 'b', 'c'])
        rc = get_unsorted_n_distinct(Question1.coeff, 6)
        cr = add_plus_sign(rc)
        # adding + for positive values for representation, keeping them separate from their actual value above.
        # note we are using first coefficient as is, regardless of its sign, only the positives are marked with + after first one
        self.q = r'${c1}{v1}{c6}{c2}{v2}{c5}{c3}{v1}{c4}{v2}$'.format(c1=cr[0], v1=self.var1, c2=cr[1], v2=self.var2,
                                                                 c3=cr[2], c4=cr[3], c5=cr[4], c6=cr[5])
        rx = add_plus_sign([rc[0]+rc[2], rc[1]+rc[3], rc[4]+rc[5]])
        self.res = r'{r1}{v1} {r2}{v2} {r3}'.format(r1=rx[0], v1=self.var1, r2=rx[1], v2=self.var2, r3=rx[2])

    def question(self):
        return "Simplfy "

    def graphic(self):
        return self.encode_graphics(self.q)

    def answer(self):
        return "{res}".format(res=self.res)

