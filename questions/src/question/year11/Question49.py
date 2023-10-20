from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
import random
from .utils import cartesian
import matplotlib.pyplot as plt
from io import BytesIO

class Question49(BaseQuestion):

    def __init__(self):
        self.type = Types.function_graph
        self.complexity = Complexity.Basic
        self.shift_y = random.sample([-3, -2, -1, 1, 2, 3],1)[0]

    def question(self):
        return ""

    def graphic(self):
        xmin, xmax, ymin, ymax = -5, 5, -5, 5
        fig, ax = cartesian(xmin, xmax, ymin, ymax)
        # Show the plot
        plt.grid(True)        
       
        ax.plot([1.0, 4.0], [0.0, 3.0], 'b')
        ax.plot([1.0, -5.0], [0.0, 5.0 ], 'b')
        shift_y_str = self.shift_y
        if self.shift_y > 0:
            shift_y_str = f'+{self.shift_y}'
        question = f'Given the graph of y=f(x), draw y=f(x) {shift_y_str}'
        ax.text(-7,5.5, question, fontsize=12)
        ax.text(4,3.2, 'y=f(x)', fontsize=12)

        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )
            
    def answer(self):
        return ""

    def answer_graphic(self):
        xmin, xmax, ymin, ymax = -5, 5, -5, 5
        fig, ax = cartesian(xmin, xmax, ymin, ymax)
        # Show the plot
        plt.grid(True)        
       
        ax.plot([1.0, 4.0], [self.shift_y+0.0, self.shift_y+3.0], 'r')
        ax.plot([1.0, -5.0], [self.shift_y+0.0, self.shift_y+5.0 ], 'r')
        shift_y_str = self.shift_y
        if self.shift_y > 0:
            shift_y_str = f'+{self.shift_y}'
        question = f'Given the graph of y=f(x), draw y=f(x) {shift_y_str}'
        ax.text(-7,5.5, question, fontsize=12)

        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )
