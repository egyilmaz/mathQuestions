from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year7.Types import Types, Complexity
from questions.src.question.utils.Utility import get_n_distinct


def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


class Question5(BaseQuestion):

    q = [8, 10, 12, 14, 16, 24, 36, 48, 54, 72, 96, 100]

    def __init__(self):
        self.type = Types.lcm
        self.complexity = Complexity.Basic
        pairs=[]
        for i in range(2):
            pairs.append(get_n_distinct(Question5.q, 2))

        self.q = f"Find the Lowest Common Multiple(LCM) of {' and '.join([str(i) for i in pairs])}"
        res = []
        for pair in pairs:
            res.append(lcm(pair[0], pair[1]))
        self.r = ' , '.join([str(i) for i in res])

    def question(self):
        return f"Factorise {self.q}"

    def answer(self):
        return f"{self.r}"

