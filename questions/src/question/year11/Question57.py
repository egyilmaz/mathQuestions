from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
import random
import sympy as sp
import matplotlib.pyplot as plt
from .utils import Vector, draw_line
from io import BytesIO

class Question57(BaseQuestion):

    def __init__(self):
        self.type = Types.vector_add
        self.complexity = Complexity.Moderate
        [self.b, self.t] = random.sample([2,3,4,5], 2)

    def question(self):
        return ""

    def graphic(self):
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.set_aspect('equal')

        # Set axis limits
        ax.set_xlim(-6, 5)
        ax.set_ylim(-6, 5)

        # Display the plot
        plt.axis('off')        
        draw_line(ax, -5,-5,0,5)
        draw_line(ax, 0,5,5,-5)
        draw_line(ax, -5,-5,5,-5)

        draw_line(ax,-3, -1, 3,-1)
        ax.text(0,5.1, 'A', fontsize=11)
        ax.text(-5.5,-5.5, 'B', fontsize=11)
        ax.text(5.5,-5.5, 'C', fontsize=11)
        ax.text(-3.5, -1, 'P', fontsize=11)
        ax.text(3.5,-1, 'R', fontsize=11)

        question = f'$\overset{{\\Delta}}{{ABC}}$ and $\overset{{\\Delta}}{{APR}}$ are similar triangles. Write $\overrightarrow{{BR}}$ in terms of $\overrightarrow{{BA}}$=a and $\overrightarrow{{BC}}$=b, where $\overrightarrow{{BP}}$ : $\overrightarrow{{PA}}$ is {self.b}:{self.t}'
        ax.text(-15,6, question, fontsize=10)

        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )
            
    def answer(self):
        return ""

    def answer_graphic(self):
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.set_aspect('equal')

        # Set axis limits
        ax.set_xlim(-6, 5)
        ax.set_ylim(-6, 5)

        # Display the plot
        plt.axis('off')        
        draw_line(ax, -5,-5,0,5)
        draw_line(ax, 0,5,5,-5)
        draw_line(ax, -5,-5,5,-5)

        draw_line(ax,-3, -1, 3,-1)
        ax.text(0,5.1, 'A', fontsize=11)
        ax.text(-5.5,-5.5, 'B', fontsize=11)
        ax.text(5.5,-5.5, 'C', fontsize=11)
        ax.text(-3.5, -1, 'P', fontsize=11)
        ax.text(3.5,-1, 'R', fontsize=11)

        va = Vector(-5,-5,-3,-1)
        va.draw(ax)
        vb = Vector(-3,-1, 3, -1, color='green')
        vb.draw(ax)

        vc= va.add(vb)
        vc.draw(ax)

        a = sp.symbols('a')
        b = sp.symbols('b')
        pr = sp.nsimplify(a*(self.b)/(self.b+self.t),rational=True)
        bp = sp.nsimplify(b*(self.t)/(self.b+self.t),rational=True)
        question = f'$\overrightarrow{{BR}}$ = $\overrightarrow{{BP}} + \overrightarrow{{PR}} = {{{pr}}} + {{{bp}}}$'
        ax.text(-15,6, question, fontsize=10)

        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )
