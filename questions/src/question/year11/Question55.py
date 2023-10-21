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
        self.shift_x = random.sample([-3, -2, -1, 1, 2, 3],1)[0]

    def question(self):
        return ""

    def graphic(self):
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.set_aspect('equal')

        # Set axis limits
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 4)

        # Display the plot
        plt.axis('off')        

        question = f'Given below vector, draw its horizontal and vertical components'
        ax.text(0,4, question, fontsize=10)
        v1 = Vector(1.0, 0, 3.0, 3.0)
        v1.draw(ax)

        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )
            
    def answer(self):
        return ""

    def answer_graphic(self):
        fig, ax = plt.subplots(figsize=(4, 4))
        ax.set_aspect('equal')

        # Set axis limits
        ax.set_xlim(0, 7)
        ax.set_ylim(-1, 4)

        # Display the plot
        plt.axis('off')        
        v1 = Vector(1.0, 0, 3.0, 3.0)
        v1.draw(ax)
        v1x = Vector(1.0, 0, 3.0, 0.0,color='red')
        v1x.draw(ax)
        v1y = Vector(1.0, 0, 1.0, 3.0,color='red')
        v1y.draw(ax)

        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )
