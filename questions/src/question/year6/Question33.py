from questions.src.question.BaseQuestion import BaseQuestion
from datetime import timedelta,datetime
import random
from questions.src.question.Types import Types, Complexity


class Question33(BaseQuestion):
    def __init__(self):
        self.type = Types.Time_24hr_am_pm
        self.complexity = Complexity.Basic
        delta = random.choice([1,2,3,4,0.75,0.2,0.5,0.8])
        self.start = datetime.now() + timedelta(hours=delta)
        self.start_str="{0}:{1}".format(self.start.hour, self.start.minute)
        self.body = "What will be the 24hr formatted {0} time, in am/pm form?".format(self.start_str)
        self.res= self.start.strftime('%I:%M %p')

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
