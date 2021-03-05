import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.resources.Resource import girls
from questions.src.question.Types import Types, Complexity


class Question59(BaseQuestion):
    def __init__(self):
        self.type = Types.Money
        self.complexity = Complexity.Moderate
        self.subject = random.choice(girls)
        self.count = random.choice([2,3,4])
        self.coins = []
        for i in range(0,self.count):
            self.coins.append(random.choice([1,2,5,10,20,50]))

        self.total=0
        for coin in self.coins:
            self.total += coin

        self.body = "{subj} has {count} coins (in pences) in her hand. There might be more than one of the same coin. She knows its a total of {total}, can you identify which coins are these?"\
            .format(subj=self.subject, count=self.count, total=self.total)

    def question(self):
        return self.body

    def answer(self):
        return "{subj} has {coins}".format(subj=self.subject, coins=self.coins)
