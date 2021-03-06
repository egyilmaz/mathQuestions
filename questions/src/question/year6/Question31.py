import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.resources.Resource import places, subjects
from questions.src.question.utils.Utility import get_n_distinct
from datetime import timedelta,datetime
from questions.src.question.year6.Types import Types, Complexity


class Question31(BaseQuestion):
    def __init__(self):
        self.type = [Types.Time_add]
        self.complexity = Complexity.Basic
        self.place = random.choice(places)
        self.subj1, self.subj2 = get_n_distinct(subjects,2)
        self.start = datetime.now()
        self.start_str="{0}:{1}".format(self.start.hour, self.start.minute)
        hrs = random.choice([1,2,3,4])
        delta= timedelta(hours=hrs)
        seconds = delta.total_seconds()
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        self.spent = ""
        if hours!=0:
            self.spent = "{0} hours ".format(int(hours))
        if minutes!=0:
            self.spent = self.spent + "{0} minutes ".format(int(minutes))
        self.body = "{0} and {1} met at the {2} at {3}. If they spent {4} visiting the place, when do they leave. ".format(self.subj1, self.subj2, self.place,self.start_str,self.spent)
        result = (self.start + delta)
        self.res = "They leave at {0}:{1}".format(result.hour,result.minute)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
