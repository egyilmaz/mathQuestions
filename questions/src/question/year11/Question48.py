from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
import random
import matplotlib.pyplot as plt
from io import BytesIO

class Question48(BaseQuestion):

    def __init__(self):
        self.type = Types.circle
        self.complexity = Complexity.Basic
        self.theta = random.sample([100, 110, 120, 130],1)[0]
        self.q = f""
        beta = (360 - 2*self.theta) / 2
        self.res= f"$\\beta$={beta}"

    def question(self):
        return ""

    def graphic(self):
        fig, ax = plt.subplots(figsize=(4,4))

        # Draw a circle
        circle = plt.Circle((0, 0), 1, fill=False)
        ax.add_patch(circle)

        # Plot the red lines
        ax.plot([0, 0.5], [0, 0.86], 'r')
        ax.plot([0, 0.3], [0, -0.95], 'r')

        # Plot the blue lines
        ax.plot([0.5, 2.2], [0.87, -0.3], 'b')
        ax.plot([0.3, 2.2], [-0.96, -0.3 ], 'b')
        theta = f"$\\theta$"
        beta = f"$\\beta$"
        ax.text(0.2,-0.1, theta, fontsize=14)
        ax.text(1.6,-0.3, beta, fontsize=14)
        ax.text(-0.2,0,'O', fontsize=12)
        ax.set_title(f"Given {theta}={self.theta} and O is the center of the circle, find {beta}",fontsize=10)
        # Set axis limits
        ax.set_xlim(-1.2, 2.3)
        ax.set_ylim(-1.2, 1.2)

        # Set aspect ratio to equal
        ax.set_aspect('equal', adjustable='box')

        # Show the plot
        plt.gca().set_aspect('equal', adjustable='box')
        plt.axis('off')
        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )        

    def answer(self):
        return ""

    def answer_graphic(self):
        return self.encode_graphics(self.res)
