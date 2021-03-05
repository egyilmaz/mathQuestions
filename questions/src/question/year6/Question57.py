import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.resources.Resource import boys
from questions.src.question.utils.Utility import get_n_distinct
from questions.src.question.Types import Types, Complexity


class Question57(BaseQuestion):
    def __init__(self):
        self.type = Types.Money
        self.complexity = Complexity.Basic
        self.subject = random.choice(boys)
        self.count = random.choice([2,3])
        self.coins = get_n_distinct([1,2,5,10], self.count)
        self.total=0
        for coin in self.coins:
            self.total += coin
        self.body = "{subj} has {count} unique coins (in pences) in his hand. He knows its a total of {total}, can you identify which coins are these?"\
            .format(subj=self.subject, count=self.count, total=self.total)

    def question(self):
        return self.body

    def answer(self):
        return "{subj} has {coins}".format(subj=self.subject, coins=self.coins)
