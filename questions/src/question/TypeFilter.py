from .BaseFilter import BaseFilter


class TypeFilter(BaseFilter):
    def __init__(self, qtype):
        self.qtype = qtype

    def filter(self, q):
        return self.qtype.lower() in str(q.type).lower()