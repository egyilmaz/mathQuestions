from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
import random
import matplotlib.pyplot as plt
from .utils import Vector, cartesian
from io import BytesIO

class Question56(BaseQuestion):

    def __init__(self):
        self.type = Types.vector_add
        self.complexity = Complexity.Basic
        theList=[(Vector(3, 3, 1, 0),  Vector(1, 0, -4, 3)),
                 (Vector(2, 2, 1, 0),  Vector(1, 0, -3, 5)),
                 (Vector(0, 0, -2, 2),  Vector(0, 0, -2, -2)),
                 (Vector(0, 0, -2, -2),  Vector(0, 0, 2, -2)),
                 (Vector(1, 0, -3, 5), Vector(1, 0, -1, -2))
                 ]
        self.v1, self.v2 = random.sample(theList, 1)[0]

    def question(self):
        return ""

    def graphic(self):
        fig,ax = cartesian(-6, 6, -6, 6)
        self.v1.draw(ax)
        self.v2.draw(ax)
        question = f'Add the two vectors given below'
        ax.text(-6,5.5, question, fontsize=10)

        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )
            
    def answer(self):
        return ""

    def answer_graphic(self):
        fig, ax = plt.subplots(figsize=(4, 4))
        ax.set_aspect('equal')

        # Set axis limits
        ax.set_xlim(-6, 5)
        ax.set_ylim(-5, 5)

        # Display the plot
        plt.axis('off')        

        self.v1.draw(ax)
        self.v2.draw(ax)
        v3 =self.v1.add(self.v2)
        v3.draw(ax)

        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )
