import random
from fractions import Fraction
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_two_distinct
from questions.src.question.year6.Types import Types, Complexity


class Question40(BaseQuestion):
    def __init__(self):
        self.type = Types.Percentage
        self.complexity = Complexity.Advanced
        self.school = random.choice([200,300,400,500])
        self.per1,self.per2 = get_two_distinct([2,3,4,5,10,15,20,25])
        self.lang1,self.lang2 = get_two_distinct(["German","Turkish","Mandarin","French","Arabic","Spanish","Russian"])
        self.body = "In a school of {school} students, {per1}% of the students study {lang1} and {per2}% of the students study {lang2}."\
                    "How many of the students study neither of these languages?"\
            .format(school=self.school, per1=self.per1, lang1=self.lang1, per2=self.per2, lang2=self.lang2)
        self.res = self.school*( 1 - Fraction(self.per1,100) - Fraction(self.per2,100) )
    def question(self):
        return self.body

    def answer(self):
        return "{res} many students study neither of those languages".format(res=self.res)
