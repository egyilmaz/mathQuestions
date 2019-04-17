from .TypeFilter import TypeFilter
from .ComplexityFilter import ComplexityFilter

class FilterFactory():
    def __init__(self):
        self.filters=[]

    def appendTypeFilter(self, qtype):
        if qtype:
            self.filters.append(TypeFilter(qtype))

    def appendComplexityFilter(self,complexity):
        if complexity:
            self.filters.append(ComplexityFilter(complexity))

    def run_filters(self,q):
        filter_result = True  # in absence of any filter, append all.
        for f in self.filters:
            filter_result = filter_result and f.filter(q)
        return filter_result

