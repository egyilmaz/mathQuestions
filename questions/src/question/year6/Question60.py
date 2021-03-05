import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_n_distinct
from questions.src.question.year6.Types import Types, Complexity


class Question60(BaseQuestion):
    def __init__(self):
        self.type = Types.Percentage
        self.complexity = Complexity.Moderate
        self.percentages = get_n_distinct([1,2,5,7,8,9,10,20,50],4)
        self.languages = get_n_distinct(["German","Turkish","Mandarin","Spanish","Arabic","Urdu","Hindu"],4)
        self.population = random.choice([1000,2000,3000])
        self.spoken = [(self.population/100)*per for per in self.percentages]
        self.body = "In a school with {pop} students".format(pop=self.population)
        c=0
        for p in self.spoken:
            self.body += ", {many} speaks {lang}".format(many=p, lang=self.languages[c])
            c += 1
        self.body += ". What are the percentages of these students speaking these languages?"

    def question(self):
        return self.body

    def answer(self):
        return "{0}".format(self.percentages)
