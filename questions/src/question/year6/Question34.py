from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.resources.Resource import items,girls
import random
from questions.src.question.year6.Types import Types, Complexity


class Question34(BaseQuestion):
    def __init__(self):
        self.type = Types.Percentage
        self.complexity = Complexity.Advanced
        self.subj = random.choice(girls)
        self.profit = random.choice([10,20,25,50])
        self.bought = random.choice([20,40,60,80])
        self.item = random.choice(items)
        self.body = "{0} is planning to sell {1} she bought for {2} pounds with {3}% profit, What is the selling price?".format(self.subj, self.item, self.bought, self.profit)
        selling_price = self.bought *(1+ self.profit/100)
        self.res = "Selling price is {0}".format(selling_price)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
