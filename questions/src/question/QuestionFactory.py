from .utils.Utility import get_n_distinct
from .Types import Types, Complexity
from .FilterFactory import FilterFactory
import logging
logger = logging.getLogger(__name__)


class QuestionFactory:

    def load_all_questions(self, year=6):
        result=[]
        nof_registered_questions = self.get_nof_questions(year)
        for i in range(0,nof_registered_questions):
            result.append(self.__get_question__(i, year))
        return result


    def statistics(self, types_enabled, complexity_enabled, year=6):
        nof_registered_questions = self.get_nof_questions(year)
        nof_q = "There are {0} different questions<br>".format(nof_registered_questions)
        all_questions = self.load_all_questions(year)
        types_dict={}
        complexities_dict={}
        for q in all_questions:
            if types_enabled:
                if "enum" in str(type(q.type)): #single enum type question
                    types_dict[q.type] = types_dict.get(q.type,0) + 1
                else: # some questions are qualified with more than one type, list of enums
                    for typ in q.type:
                        types_dict[typ] = types_dict.get(typ, 0) + 1

            if complexity_enabled:
                complexities_dict[q.complexity] = complexities_dict.get(q.complexity,0)+1
            #logger.error("ahanda comp "+str(q.complexity))

        types_str=""
        if types_enabled:
            for typ in Types:
                types_str += "{0}:{1}<br>".format(str(typ),types_dict.get(typ,0))

        complexities_str=""
        if complexity_enabled:
            for cp in Complexity:
                complexities_str += "{0}:{1}<br>".format(str(cp),complexities_dict.get(cp,0))

        return nof_q + types_str + complexities_str

    def ask_filtered(self, nof_questions, qtype, complexity, year=6):
        ff = FilterFactory()
        ff.appendTypeFilter(qtype)
        ff.appendComplexityFilter(complexity)

        candidates=[]
        nof_registered_questions = self.get_nof_questions(year)
        for i in range(0,nof_registered_questions):
            q = self.__get_question__(i, year)
            if ff.run_filters(q):
                candidates.append(i) # indexes matching criteria is stored in array
        return self.get_bunch(nof_questions, candidates, year)

    def ask_question(self, nof_questions, start, end, year):
        start = max(0, start - 1) # question index starts from zero, requests start from 1
        return self.get_bunch(nof_questions, range(start,end), year)

    def get_bunch(self,nof_questions, rng, year=6):
        nof_req = len(rng)
        if nof_req == 0:
            return []
        nof_group = int(nof_questions/nof_req)
        nof_rem = nof_questions % nof_req
        #logger.error('noq{3}, req{0} grp{1}, rem{2}'.format(nof_req, nof_group, nof_rem, nof_questions))
        #say we have 12 registered questions, we want 34 questions starting from 5, ending at 10
        #nof_req = 10 - 5 , questions from 5 to 10 are requested, 5 different question type
        #nof_group = 34 / 5, 6 groups of 5 question type
        #nof_rem = 34 % 5, 4 questions from 5 question type
        bunch = []
        for i in range(0, nof_group):
            bunch = bunch + get_n_distinct(rng,nof_req)
        bunch = bunch + get_n_distinct(rng,nof_rem)
        result = []
        for i in bunch:
            result.append(self.__get_question__(i, year))
        return result

#    def ask_printed(self, nof_questions):
#        self.sheet_number = self.sheet_number + 1
#        postfix = str(self.sheet_number) + '.txt'
#        with open('answers_' + postfix, 'w') as file_a, open('questions_' + postfix, 'w') as file_q:
#            for i in range(0, nof_questions):
#                q = self.__get_question__(i % nof_registered_questions)
#                file_q.write(str(i+1) + ') ' + q.question())
#                file_q.write('\n\n\n\n\n')
#                file_a.write(str(i+1) + ') ' + ', '.join("{}: {}".format(k, str(v)) for k, v in q.result().items()))
#                file_a.write('\n')

    @staticmethod
    def get_nof_questions(year):
        if year == 6:
            from questions.src.question.year6.registry import get_nof_questions
            return get_nof_questions()
        if year == 7:
            from questions.src.question.year7.registry import get_nof_questions
            return get_nof_questions()

    @staticmethod
    def __get_question__(qtype, year=6):
        if year == 6:
            from questions.src.question.year6.registry import get_question
            return get_question(qtype)
        if year == 7:
            from questions.src.question.year7.registry import get_question
            return get_question(qtype)
