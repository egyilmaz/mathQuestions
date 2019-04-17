from .utils.Utility import get_n_distinct
from .Types import Types, Complexity
from .FilterFactory import FilterFactory
import logging
logger = logging.getLogger(__name__)

nof_registered_questions = 36

class QuestionFactory:

    def load_all_questions(self):
        result=[]
        for i in range(0,nof_registered_questions):
            result.append(self.__get_question__(i))
        return result


    def statistics(self, types_enabled, complexity_enabled):
        nof_q = "There are {0} different questions<br>".format(nof_registered_questions)
        all_questions = self.load_all_questions()
        types_dict={}
        complexities_dict={}
        for q in all_questions:
            if types_enabled:
                types_dict[q.type] = types_dict.get(q.type,0) + 1
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

    def ask_filtered(self, nof_questions, qtype, complexity):
        ff = FilterFactory()
        ff.appendTypeFilter(qtype)
        ff.appendComplexityFilter(complexity)

        candidates=[]
        for i in range(0,nof_registered_questions):
            q = self.__get_question__(i)
            if ff.run_filters(q):
                candidates.append(i) # indexes matching criteria is stored in array
        return self.get_bunch(nof_questions, candidates)

    def ask_question(self, nof_questions, start, end):
        start = max(0, start - 1) # question index starts from zero, requests start from 1
        return self.get_bunch(nof_questions, range(start,end))

    def get_bunch(self,nof_questions, rng):
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
            result.append(self.__get_question__(i))
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
    def __get_question__(qtype):
        if qtype == 0:
            from .Question1 import Question1
            return Question1()
        if qtype == 1:
            from .Question2 import Question2
            return Question2()
        if qtype == 2:
            from .Question3 import Question3
            return Question3()
        if qtype == 3:
            from .Question4 import Question4
            return Question4()
        if qtype == 4:
            from .Question5 import Question5
            return Question5()
        if qtype == 5:
            from .Question6 import Question6
            return Question6()
        if qtype == 6:
            from .Question7 import Question7
            return Question7()
        if qtype == 7:
            from .Question8 import Question8
            return Question8()
        if qtype == 8:
            from .Question9 import Question9
            return Question9()
        if qtype == 9:
            from .Question10 import Question10
            return Question10()
        if qtype == 10:
            from .Question11 import Question11
            return Question11()
        if qtype == 11:
            from .Question12 import Question12
            return Question12()
        if qtype == 12:
            from .Question13 import Question13
            return Question13()
        if qtype == 13:
            from .Question14 import Question14
            return Question14()
        if qtype == 14:
            from .Question15 import Question15
            return Question15()
        if qtype == 15:
            from .Question16 import Question16
            return Question16()
        if qtype == 16:
            from .Question17 import Question17
            return Question17()
        if qtype == 17:
            from .Question18 import Question18
            return Question18()
        if qtype == 18:
            from .Question19 import Question19
            return Question19()
        if qtype == 19:
            from .Question20 import Question20
            return Question20()
        if qtype == 20:
            from .Question21 import Question21
            return Question21()
        if qtype == 21:
            from .Question22 import Question22
            return Question22()
        if qtype == 22:
            from .Question23 import Question23
            return Question23()
        if qtype == 23:
            from .Question24 import Question24
            return Question24()
        if qtype == 24:
            from .Question25 import Question25
            return Question25()
        if qtype == 25:
            from .Question26 import Question26
            return Question26()
        if qtype == 26:
            from .Question27 import Question27
            return Question27()
        if qtype == 27:
            from .Question28 import Question28
            return Question28()
        if qtype == 28:
            from .Question29 import Question29
            return Question29()
        if qtype == 29:
            from .Question30 import Question30
            return Question30()
        if qtype == 30:
            from .Question31 import Question31
            return Question31()
        if qtype == 31:
            from .Question32 import Question32
            return Question32()
        if qtype == 32:
            from .Question33 import Question33
            return Question33()
        if qtype == 33:
            from .Question34 import Question34
            return Question34()
        if qtype == 34:
            from .Question35 import Question35
            return Question35()
        if qtype == 35:
            from .Question36 import Question36
            return Question36()