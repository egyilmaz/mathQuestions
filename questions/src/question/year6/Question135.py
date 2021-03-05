import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.Types import Types, Complexity


class Question135(BaseQuestion):
    def __init__(self):
        self.type = [Types.General_Problem, Types.sat_reasoning]
        self.complexity = Complexity.Advanced
        times = random.choice([1.5,2.5,3.5,4.5])
        first = random.choice([4752, 5468, 3456, 4326])
        sel = random.choice([2, 5, 10, 100])
        res = int(times*first)
        self.body = "Given {0} x {1} = {2} How can you calculate {2} / {3}"\
            .format(times, first, res,  int(times*sel))

        self.res="{0} divided by {1}".format(first,sel)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
