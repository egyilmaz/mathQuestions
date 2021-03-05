import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.Types import Types, Complexity


class Question127(BaseQuestion):
    def __init__(self):
        self.type = [Types.Ordering, Types.sat_reasoning]
        self.complexity = Complexity.Moderate
        first = random.sample([1009909, 1090999, 1023065, 1009099, 1230650, 1900009, 1023650, 1023305, 1203605],5)
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
