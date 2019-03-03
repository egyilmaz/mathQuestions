import random
from src.question.Types import Types
from src.resources.Resource import fast_vehicles, fast_speeds, duration
from src.utils.Utility import ask_interactive_1arg


class Question6:
    def __init__(self):
        self.type = Types.FIRST_ORDER_1_UNKNOWN
        self.vehicle = random.choice(fast_vehicles)
        self.speed = random.choice(fast_speeds)
        self.duration = random.choice(duration)
        self.distance = self.speed * self.duration
        self.body = "A {veh} is travelling at the speed of {spd}mph. How much distance it will cover in {hrs} hours?"\
            .format(veh=self.vehicle, spd=self.speed, hrs=self.duration)

    def question(self):
        return self.body

    def ask_user(self):
        return self.distance == ask_interactive_1arg(self.question())

    def result(self):
        return {self.vehicle: self.distance}

    def answer(self):
        return "It will travel {dist} miles".format(dist=self.distance)
