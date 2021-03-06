from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year7.Types import Types, Complexity
import random

class Question2(BaseQuestion):

    q_a = [(r'$x$+$2x^2$', 'x(1+2x)'),
           (r'$x$-$2x^2$', 'x(1-2x)'),
           (r'$x^2$+$2x$', 'x(x+2)'),
           (r'$x^2$-$2x$', 'x(x-2)'),
           (r'$4x^2$+$8x$', '4x(x+2)'),
           (r'$-x$-$x^2$', 'x(-1-x) or -x(1+x)'),
           (r'$6x$-$3x^2$', '3x(2-x)'),
           (r'$-6x^2$-$3x$', '-3x(2x+1) or 3x(-2x-1)'),
           ]
    def __init__(self):
        self.type = Types.Factorise_expression
        self.complexity = Complexity.Basic
        self.q, self.a = random.choice(Question2.q_a)

    def question(self):
        return "Factorise "

    def graphic(self):
        return self.encode_graphics(self.q)

    def answer(self):
        return "{res}".format(res=self.a)

