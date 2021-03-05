import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year6.Types import Types, Complexity
from questions.src.question.resources.Resource import boys
from questions.src.question.utils.Utility import get_two_distinct


class Question64(BaseQuestion):
    def __init__(self):
        self.type = Types.Decimal
        self.complexity = Complexity.Advanced
        self.subj = random.choice(boys)
        self.dec1, self.dec2 = get_two_distinct([0.1,0.2,0.3,0.4,0.5])
        self.hrs = random.choice([10,20,30,40,50])
        self.body = "{subj} studies a total of {hrs}hours a week. If he studies {dec1} of those hours on maths and {dec2} of those hours on science,"\
                     "How much time is left for english?".format(subj=self.subj, dec1 = self.dec1, dec2=self.dec2, hrs=self.hrs)
        self.res = self.hrs*(1-self.dec1-self.dec2)
    def question(self):
        return self.body

    def answer(self):
        return "{0} hours left for english".format(self.res)
