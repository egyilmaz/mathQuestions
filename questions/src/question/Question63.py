import random
from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity
from .resources.Resource import girls


class Question63(BaseQuestion):
    def __init__(self):
        self.type = Types.Decimal
        self.complexity = Complexity.Moderate
        self.subj = random.choice(girls)
        self.dec = random.choice([0.1,0.2,0.3])
        self.hrs = random.choice([10,20,30,40])
        self.body = "{subj} works {hrs}hours a week. If she spends {dec} of those hours in breaks, how many hours"\
                    " does she actually work? ".format(subj=self.subj, dec = self.dec, hrs=self.hrs)
        self.res = self.hrs*(1-self.dec)
    def question(self):
        return self.body

    def answer(self):
        return "She works {0} hours".format(self.res)
