import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.resources.Resource import girls
from questions.src.question.utils.Utility import get_n_distinct
from datetime import timedelta,datetime
from questions.src.question.year6.Types import Types, Complexity


class Question106(BaseQuestion):
    def __init__(self):
        self.type = [Types.Time_add, Types.sat_reasoning]
        self.complexity = Complexity.Moderate
        self.subj1 = get_n_distinct(girls,1)[0]
        self.start = datetime.now()
        self.start_str = "{0}:{1}".format(self.start.hour, self.start.minute)
        minutes = random.choice([11,22,33,44])
        delta1 = timedelta(minutes=minutes)
        self.first = random.choice([1, 2, 3])
        self.second = random.choice([1, 2, 3])
        self.third = random.choice([2, 4])
        delta2 = timedelta(minutes = 60*self.first+ self.second*60/self.third)
        result = (self.start + delta1 + delta2)
        self.res = "They leave at {0}:{1}".format(result.hour,result.minute)
        self.body="{0} starts eating her meal at {1} in a cafe. If meal took {2} minutes to eat and "\
            .format(self.subj1, self.start_str, minutes)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)

    def graphic(self):
        a = r"it takes ${0}\dfrac{{{1}}}{{{2}}}$ hours get back home, when does she arrive home. "\
            .format(self.first,self.second,self.third)
        return self.encode_graphics(a)

