from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year7.Types import Types, Complexity
import random

class Question10(BaseQuestion):

    q_a = [(r"$(x-1)^2$", r'$x^2-2x+1$'),
           (r"$(x-y)^2$", r'$x^2-2xy+y^2$'),
           (r"$(y-x)^2$", r'$y^2-2xy+x^2$'),
           (r"$(x+y)^2$", r'$x^2+2xy+y^2$'),
           (r"$(1+x)^2$", r'$1+2x+x^2$'),
           (r"$(1-t)^2$", r'$1-2t+t^2$'),
           (r"$(v+3)^2$", r'$v^2+6v+9$'),
           (r"$(f+4)^2$", r'$f^2+8f+16$'),
           (r"$(2c+1)^2$", r'$4c^2+4c+1$'),
           (r"$(2x-2)^2$", r'$4x^2-8x+4$'),
           (r"$(3x+4)^2$", r'$9x^2+24x+16$'),
           (r"$(2-3b)^2$", r'$4-12b+9b^2$'),
           (r"$(3y-3x)^2$", r'$9y^2-18xy+9x^2$'),
           (r"$(10-3a)^2$", r'$100-60a+9a^2$'),
           (r"$(5+5b)^2$", r'$25-50b+25b^2$'),
           (r"$(3+6c)^2$", r'$9+36c+36c^2$'),
           (r"$(6+2d)^2$", r'$36+24d+4d^2$'),
           (r"$(1+10e)^2$", r'$1+20e+100e^2$'),
           ]
    def __init__(self):
        self.type = Types.quadratic_basic
        self.complexity = Complexity.Basic
        self.q, self.a= random.choice(Question10.q_a)

    def question(self):
        return "Write an expression for: "

    def graphic(self):
        return self.encode_graphics(self.q)

    def answer_graphic(self):
        return self.encode_graphics(self.a)
