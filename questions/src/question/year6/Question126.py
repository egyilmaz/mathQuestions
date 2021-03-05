import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year6.Types import Types, Complexity


class Question126(BaseQuestion):
    def __init__(self):
        self.type = [Types.General_Problem, Types.sat_reasoning]
        self.complexity = Complexity.Moderate
        num = random.choice([9072, 8091, 9001, 8990])
        diff = random.choice([1000, 1001, 1010, 1100])
        wording=random.choice(['more', 'less'])
        self.body = "What number is {0} {1} than {2}?".format(diff,wording,num)
        res = num - diff
        if 'mor' in wording:
            res = num + diff
        self.res = "{0}".format(res)

    def question(self):
        return self.body

    def answer(self):
        return self.res
