from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
import random
import math

class Question52(BaseQuestion):

    def __init__(self):
        self.type = Types.ratio
        self.complexity = Complexity.Moderate
        [a,b,c] = random.sample(['x','a','b','c','u','y','w'],3)
        [av,bv,bv2,cv,cv2] = random.sample([3,4,5,6,7,8,9,10,12],5)
        cv *= cv
        cv2 *= cv2 
        self.q = f"{a} is directly proportional to {b} and {b} is directly proportional to square root of {c}. Given {a}={av}, {b}={bv} and {b}={bv2}, {c}={cv}. What is {a} when {c} is {cv2}"
        k = av/bv
        m = bv2/math.sqrt(cv)
        res = m*math.sqrt(cv2)/k
        self.res= f"{a}={res}"

    def question(self):
        return ""

    def graphic(self):
        return self.encode_graphics(self.q,  14)

    def answer(self):
        return ""

    def answer_graphic(self):
        return self.encode_graphics(self.res, 15)
