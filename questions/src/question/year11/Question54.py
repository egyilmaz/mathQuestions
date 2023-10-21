from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
import random
import matplotlib.pyplot as plt
from .utils import Vector
from io import BytesIO

class Question54(BaseQuestion):

    def __init__(self):
        self.type = Types.vector
        self.complexity = Complexity.Basic
        self.shift_x = random.sample([-3, -2, -1, 1, 2, 3],1)[0]

    def question(self):
        return ""

    def graphic(self):
        fig, ax = plt.subplots(figsize=(4, 4))
        ax.set_aspect('equal')

        # Set axis limits
        ax.set_xlim(-5, 5)
        ax.set_ylim(-1, 5)

        # Display the plot
        plt.axis('off')        

        v1 = Vector(3.0, 3.0, 1.0, 0.0)
        v1.draw(ax)
        v2 = Vector(1.0, 0.0, -4.0, 3.0)
        v2.draw(ax)
        question = f'Given vectors OA and AB, draw OA+AB'
        ax.text(-6,5.5, question, fontsize=10)
        ax.text(3.1,3.1, 'O', fontsize=12)
        ax.text(0.9,0.3, 'A', fontsize=12)
        ax.text(-4.1,3.1, 'B', fontsize=12)

        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )
            
    def answer(self):
        return ""

    def answer_graphic(self):
        fig, ax = plt.subplots(figsize=(4, 4))
        ax.set_aspect('equal')

        # Set axis limits
        ax.set_xlim(-5, 5)
        ax.set_ylim(-1, 5)

        # Display the plot
        plt.axis('off')        

        v1 = Vector(3.0, 3.0, 1.0,0.0)
        v1.draw(ax)
        v2 = Vector(1.0, 0.0, -4.0, 3.0)
        v2.draw(ax)
        question = f'Given vectors OA and AB, draw OA+AB)'
        ax.text(-6,5.5, question, fontsize=10)
        ax.text(3.1,3.1, 'O', fontsize=12)
        ax.text(0.9,0.3, 'A', fontsize=12)
        ax.text(-4.1,3.1, 'B', fontsize=12)
        v3 = Vector(3.0, 3.0, -4.0, 3.0, color='red')
        v3.draw(ax)

        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )
