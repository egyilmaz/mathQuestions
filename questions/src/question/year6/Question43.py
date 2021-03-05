import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.resources.Resource import girls
from questions.src.question.utils.Utility import get_two_distinct
from questions.src.question.Types import Types, Complexity


class Question43(BaseQuestion):
    def __init__(self):
        self.type = Types.Conversion
        self.complexity = Complexity.Advanced
        self.subject = random.choice(girls)
        self.sack1 = random.choice([1005, 1020, 1034, 1001, 1002, 1432, 1534])
        self.sack2 = random.choice([2.20, 2.38, 2.45, 3.6])
        self.item1, self.item2 = get_two_distinct(['potatoe','onion','tomatoe','lentils','flour','chickpeas'])
        self.res = self.sack2*1000 - self.sack1
        self.body="{subj} buys {sack1}gr of {item1} and {sack2}kg of {item2}. What is the weight difference between the two in grams"\
                .format(subj=self.subject,sack1=self.sack1,sack2=self.sack2,item1=self.item1, item2=self.item2)

    def question(self):
        return self.body

    def answer(self):
        return "Difference is {res}".format(res=self.res)
