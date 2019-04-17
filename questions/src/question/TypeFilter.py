from .Types import Types
from .BaseFilter import BaseFilter


class TypeFilter(BaseFilter):
    def __init__(self, qtype):
        self.qtype = qtype

    def filter(self, q):
        return q.type == Types[self.qtype]