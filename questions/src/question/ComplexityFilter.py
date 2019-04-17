from .BaseFilter import BaseFilter


class ComplexityFilter(BaseFilter):
    def __init__(self, complexity):
        self.complexity = complexity

    def filter(self, q):
        return self.complexity.lower() in str(q.complexity).lower()