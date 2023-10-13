from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
import random
import matplotlib.pyplot as plt
from matplotlib.table import Table
from io import BytesIO

class Question35(BaseQuestion):
    def __init__(self):
        self.type = [Types.boxplot]
        self.complexity = Complexity.Basic
        # Your list of numeric values
        self.box_data = random.sample([[10, 20, 50, 60, 90],
                                       [15, 40, 60, 75, 110],
                                       [40, 60, 75, 88, 140],
                                       [45, 70, 83, 99, 180],
                                       [60, 80, 89, 101, 200]],1)[0]

    def question(self):
        return ""

    def answer(self):
        return ""

    def graphic(self):
        labels = ['Minimum value', 'Lower Quartile' , 'Interquartile range', 'Median', 'Maximum value']
        data = zip(labels, self.box_data)
        # Create the table
        fig, ax = plt.subplots()
        ax.axis('off')
        table = Table(ax, bbox=[0, 0, 1, 1])

        # Add the data to the table
        for i, (text1, text2) in enumerate(data):
            table.add_cell(i, 0, 0.8, 1, text=text1, loc='center', facecolor='lightgray')
            table.add_cell(i, 1, 0.8, 1, text=text2, loc='right')

        # Add the table to the plot
        ax.add_table(table)
        # Adjust the layout to fit the table properly
        table.set_fontsize(10)
        ax.set_title(r'Draw a box plot to represent the statistics in the given table', fontsize=9)
        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )

    def answer_graphic(self):
        fig, ax = plt.subplots()
        fig.set_size_inches(6, 2, forward=True)
        max_val = 1.05*self.box_data[4]
        min_val = 0.9*self.box_data[0]
        answer_data = [self.box_data[0], self.box_data[1], self.box_data[3], self.box_data[1]+self.box_data[2], self.box_data[4]]
        ax.boxplot(answer_data, vert=False)
        ax.set_yticks([])  # Hide the y-axis labels
        ax.set_xlim(min_val, max_val) 
        # Set custom x-axis ticks for the box plot
        ax.set_xticks(answer_data)
        plt.xticks(fontsize=8)

        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )
