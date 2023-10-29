from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
import random
from .utils import cartesian, Vector
import matplotlib.pyplot as plt
from io import BytesIO

class Question55(BaseQuestion):

    def __init__(self):
        self.type = Types.vector
        self.complexity = Complexity.Basic
        theList=[Vector(3, 3, 1, 0),  Vector(1, 0, -4, 3),
                 Vector(2, 2, 1, 0),  Vector(1, 0, -3, 5),
                 Vector(0, 0, -2, 2),  Vector(0, 0, -2, -2),
                 Vector(0, 0, 3, 0),  Vector(0, 0, -4, 0),
                 Vector(0, 0, -3, 0),  Vector(0, 0, 5, 0),
                 Vector(0, 0, -2, -2),  Vector(0, 0, 2, -2),
                 Vector(1, 0, -3, 5), Vector(1, 0, -1, -2)
                 ]
        self.v = random.sample(theList,1)[0]

    def question(self):
        return ""

    def graphic(self):
        fig,ax = cartesian(-6, 6, -6, 6)

        question = f'Given below vector, draw its horizontal and vertical components'
        ax.text(0,4, question, fontsize=10)
        self.v.draw(ax)

        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )
            
    def answer(self):
        return ""

    def answer_graphic(self):
        fig,ax = cartesian(-6, 6, -6, 6)
        self.v.draw(ax)
        vx = Vector(self.v.x_start, self.v.y_start, self.v.x_end, self.v.y_start,color='red')
        vx.draw(ax)
        vy = Vector(self.v.x_start, self.v.y_start, self.v.x_start, self.v.y_end,color='red')
        vy.draw(ax)

        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )
