from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
import random
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from .utils import cartesian

class Question46(BaseQuestion):

    def __init__(self):
        self.type = Types.parabola
        self.complexity = Complexity.Moderate
        theList = list(range(-5,5))
        self.r1 =random.sample(theList,1)[0]
        self.r2 =random.sample(theList,1)[0]
        self.a = random.sample([2,3,4],1)[0] 
        self.b = self.a*(-self.r1-self.r2)
        self.c = self.a*(-self.r1)*(-self.r2)
        self.q = f"A parabola is crossing the x axis at {self.r1} and {self.r2}, its y intercept is at {self.c}. if its formula is $y=ax^2+bx+c$, Find the values of a,b and c"
        self.res= f"asdf"

    def question(self):
        return ""

    def graphic(self):
        return self.encode_graphics(self.q,  14)

    def answer(self):
        return ""

    def answer_graphic(self):
        xmin, xmax, ymin, ymax = -30, 30, -30, 30
        fig, ax = cartesian(xmin, xmax, ymin, ymax,([self.r1, self.r2],[self.c]))
        # Show the plot
        plt.grid(True)        
       
        # Generate a range of x-values
        x = np.linspace(-10, 10, 100)

        # Calculate the corresponding y-values for the parabola
        y = self.a*x**2 + self.b*x + self.c

        # Plot the parabola
        b = str(self.b)
        if self.b > 0:
            b = f"+{self.b}"
        c = str(self.c)
        if self.c > 0:
            c = f"+{self.c}"
        label = f'y = {self.a}$x^2$ {b}x {c}'
        ax.plot(x, y, label=label, color='b')

        # Customize the plot (labels, title, grid, etc.)
        ax.legend()

        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )        
