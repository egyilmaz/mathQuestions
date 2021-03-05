import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year6.Types import Types, Complexity


class Question107(BaseQuestion):
    def __init__(self):
        self.type = [Types.Ordering, Types.sat_reasoning]
        self.complexity = Complexity.Moderate
        first = random.sample([0.008, 0.9, 0.07, 0.12, 0.3, 2.3, 1.9, 1.09, 2.5, 2.51, 2.15, 0.426, 4.02, 4.26, 2.13,
                                2.013, 2.03, 2.134],5)
        wording = random.choice(['increasing','ascending','decreasing','descending'])
        self.body = "Given mixed number {0}, put these in {1} order".format(first,wording)
        if "incr" in wording or "asc" in wording:
            first.sort()
        else:
            first.sort(reverse=True)
        self.res="{0}".format(first)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
