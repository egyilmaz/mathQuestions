import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.Types import Types, Complexity


class Question111(BaseQuestion):
    def __init__(self):
        self.type = [Types.Problem_solving, Types.sat_reasoning]
        self.complexity = Complexity.Advanced
        can_price = random.choice([100, 150, 170, 190])
        can_amount = random.choice([25,45,65,90])
        bean_price = random.choice([240, 380, 290, 190, 210])
        tomato_price = random.choice([120,250,340,470])
        self.body = "For a can of baked bean, we need a can, 100grs of beans, 50grs of tomato. If the tomatoes " \
                    "cost {0}pence per 500gr, beans cost {1}pence per kg and cans cost {2}pence for a bundle of 10 can" \
                    ", what will be the cost of {3} cans of baked beans in pounds and pence"\
            .format(tomato_price, bean_price, can_price, can_amount)
        result = can_amount*(tomato_price/10 + bean_price/10 + can_price/10)
        self.res="{0}pound {1}pence".format(result//100, result%100)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
