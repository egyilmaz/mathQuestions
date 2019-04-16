import random
from .BaseQuestion import BaseQuestion
from .resources.Resource import fast_vehicles, fast_speeds, duration
from .Types import Types, Complexity


class Question6(BaseQuestion):
    def __init__(self):
        self.type = Types.Vehicle_speed_time_distance
        self.complexity = Complexity.Basic
        self.vehicle = random.choice(fast_vehicles)
        self.speed = random.choice(fast_speeds)
        self.duration = random.choice(duration)
        self.distance = self.speed * self.duration
        self.body = "A {veh} is travelling at the speed of {spd}mph. How much distance it will cover in {hrs} hours?"\
            .format(veh=self.vehicle, spd=self.speed, hrs=self.duration)

    def question(self):
        return self.body

    def answer(self):
        return "It will travel {dist} miles".format(dist=self.distance)
