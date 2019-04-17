from .Types import Complexity
from .BaseFilter import BaseFilter


class ComplexityFilter(BaseFilter):
    def __init__(self, complexity):
        self.complexity = complexity

    def filter(self, q):
        return q.complexity == Complexity[self.complexity]