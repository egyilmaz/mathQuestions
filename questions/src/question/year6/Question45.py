import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year6.Types import Types, Complexity


class Question45(BaseQuestion):
    def __init__(self):
        self.type = Types.Conversion
        self.complexity = Complexity.Moderate
        self.basic = random.choice([2,3,4,5,6])
        self.moderate = random.choice([2.1,3.2,3.4,3.6])
        self.advanced = random.choice([10,2,123,909])
        self.body = "Convert {bas}meter to cm, {mod}km to meter, {adv}cm to meter".format(bas=self.basic,mod=self.moderate,adv=self.advanced)
        self.res="{0}cm,{1}m,{2}m".format(self.basic*100.0,self.moderate*1000.0,self.advanced/100.0)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
