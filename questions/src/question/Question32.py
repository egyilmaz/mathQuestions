import random
from .BaseQuestion import BaseQuestion
from .resources.Resource import places, subjects
from datetime import timedelta,datetime

class Question32(BaseQuestion):
    def __init__(self):
        self.place = random.choice(places)
        self.subj1 = random.choice(subjects)
        self.start = datetime.now()
        self.start_str="{0}:{1}".format(self.start.hour, self.start.minute)
        hrs = random.choice([0.1,0.2,0.3,0.5,0.75,0.25,1,1.5,2,2.5,3,3.5,4])
        delta= timedelta(hours=hrs)
        seconds = delta.total_seconds()
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        self.ahead = ""
        if hours!=0:
            self.ahead = "{0} hours ".format(int(hours))
        if minutes!=0:
            self.ahead = self.ahead + "{0} minutes ".format(int(minutes))
        self.body = "{0} has a watch which shows {1} ahead of time. If its showing {2}, what is the actual time?".format(self.subj1, self.ahead, self.start_str)
        result = (self.start - delta)
        self.res = "It is {0}:{1}".format(result.hour,result.minute)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
