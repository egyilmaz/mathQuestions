import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year6.Types import Types, Complexity
import roman


class Question108(BaseQuestion):
    def __init__(self):
        self.type = [Types.Roman_numerals, Types.sat_reasoning]
        self.complexity = Complexity.Moderate
        first,second = random.sample([1001, 101, 99, 90, 100, 2019, 2020, 2009, 1976],2)
        self.body = "Write {0} in roman and {1} in number".format(first, roman.toRoman(second))
        self.res="{0} and {1}".format(roman.toRoman(first),second)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
