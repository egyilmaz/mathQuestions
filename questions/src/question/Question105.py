import random
from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity
from num2words import num2words


class Question105(BaseQuestion):
    def __init__(self):
        self.type = [Types.Arithmetic,Types.sat_reasoning]
        self.complexity = Complexity.Moderate
        first = random.choice([101, 202, 303, 404, 403, 304, 506])
        times = random.choice([2, 5, 10, 100])
        number = num2words(first).replace("-", " ")
        self.body = "Find the number, that is {0} times larger than {1}, write your answer in numbers and words".format(times, number)
        self.res="{0} {1}".format(first*times, num2words(first*times).replace("-"," "))

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
