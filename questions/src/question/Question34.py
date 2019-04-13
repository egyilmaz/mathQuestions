from .BaseQuestion import BaseQuestion
from .resources.Resource import items,girls
import random


class Question34(BaseQuestion):
    def __init__(self):
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
