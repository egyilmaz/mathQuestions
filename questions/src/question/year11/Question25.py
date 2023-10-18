from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
import random
import matplotlib.pyplot as plt
from io import BytesIO
from .utils import cartesian, rotate, draw_triangle

class Question25(BaseQuestion):
    def __init__(self):
        self.type = [Types.translate_rotate]
        self.complexity = Complexity.Basic
        self.x = [1, 4, 2]
        self.y = [2, 4, 4]
        self.ang = random.choice([90, 180, 270])
        self.r_x,self.r_y = random.choice([(0,0)])
        self.body = f"Draw the new figure, if we rotate the coordinate system by {self.ang} angles around ({self.r_x},{self.r_y})"

    def question(self):
        return self.body

    def answer(self):
        return ""

    def graphic(self):
        xmin, xmax, ymin, ymax = -5, 5, -5, 5
        fig, ax = cartesian(xmin, xmax, ymin, ymax)
        draw_triangle(self.x, self.y)
        # Show the plot
        plt.grid(True)        
       
        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )

    def answer_graphic(self):
        xmin, xmax, ymin, ymax = -5, 5, -5, 5
        fig, ax = cartesian(xmin, xmax, ymin, ymax)
        draw_triangle(self.x, self.y)

        new_vertices = rotate(self.x,self.y, self.ang, (self.r_x,self.r_y))
        # Extract the new x and y coordinates
        new_x, new_y = new_vertices
        plt.plot(new_x.tolist() + [new_x[0]], new_y.tolist() + [new_y[0]], marker='o', linestyle='-')

        # Show the plot
        plt.grid(True)        

        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )
