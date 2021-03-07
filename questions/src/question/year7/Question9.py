from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year7.Types import Types, Complexity
import random

class Question9(BaseQuestion):

    q_a = [(r"A number added to 5", r'$5+b$'),
           (r"Add five to a number", r'$a+5$'),
           (r"A number added to six then times by three", r'$3(6+z)$'),
           (r"A number divided by another", r'$a/b$'),
           (r"A number added to two times another number all multipled by five", r'$5(x + 2t)$ or $5a+10b$'),
           (r"A number added ten all squared", r'$(r+10)^2$'),
           (r"A number divided by six added to three then all times by five", r'$5(a/6 + 3)$'),
           (r"Five times a number added to two times another number", r'$5r + 2y$'),
           (r"A number times by three then added six", r'$3x+6$'),
           (r"A number times by three then all squared", r'$(3x)^2$ or $9x^2$'),
           (r"A number divided by another number then times by seven", r'$7(x/y)$ or $(7x)/y$'),
           (r"A number times by itself then times by three", r'$3x^2$'),
           (r"Difference between two square numbers", r'$a^2 - b^2$'),
           (r"Sum of squares of two numbers", r'$c^2 + d^2$'),
           (r"Subtract the two times the multiplication of two numbers from the sum of the squares of those numbers", r'$x^2 -2xy + y^2$'),
           (r"Subtract three from a number then divide all by 5", r'$(x-5)/3$'),
           ]
    def __init__(self):
        self.type = Types.word_expression
        self.complexity = Complexity.Basic
        self.q, self.a= random.choice(Question9.q_a)

    def question(self):
        return "Write an expression for: "+self.q

    def answer_graphic(self):
        return self.encode_graphics(self.a)
