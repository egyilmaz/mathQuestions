from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year7.Types import Types, Complexity
from questions.src.question.utils.Utility import get_n_distinct


def hcf(x, y):
   if x > y:
       smaller = y
   else:
       smaller = x
   for i in range(1,smaller + 1):
       if((x % i == 0) and (y % i == 0)):
           hcf = i
   return hcf


class Question4(BaseQuestion):

    q = [24, 36, 48, 54, 72, 96, 100, 144, 121, 128, 256, 512, 1024]

    def __init__(self):
        self.type = Types.hcf
        self.complexity = Complexity.Basic
        pairs=[]
        for i in range(2):
            pairs.append(get_n_distinct(Question4.q, 2))

        self.q = f"Find the Highest Common Factor(HCF) (also known as Greatest Common Divisor(GCD)) of {' and '.join([str(i) for i in pairs])}"
        res = []
        for pair in pairs:
            res.append(hcf(pair[0], pair[1]))
        self.r = ' , '.join([str(i) for i in res])

    def question(self):
        return f"Factorise {self.q}"

    def answer(self):
        return f"{self.r}"

