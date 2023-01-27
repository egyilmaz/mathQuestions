from .BaseFilter import BaseFilter

class TypeFilter(BaseFilter):
    def __init__(self, qtype):
        self.qtype = qtype

    def filter(self, q):
        if "enum" in str(type(q.type)):
            return self.qtype.lower() in str(q.type).lower()
        else:
            type_list = [t for t in q.type if str(self.qtype).lower() in str(t).lower()]
            return len(type_list)!=0 #non-zero type_list means we have a match
