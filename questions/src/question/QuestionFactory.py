from .utils.Utility import get_n_distinct
from .Types import Types, Complexity
from .FilterFactory import FilterFactory
import logging
logger = logging.getLogger(__name__)

nof_registered_questions = 128

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
        if qtype == 36:
            from .Question37 import Question37
            return Question37()
        if qtype == 37:
            from .Question38 import Question38
            return Question38()
        if qtype == 38:
            from .Question39 import Question39
            return Question39()
        if qtype == 39:
            from .Question40 import Question40
            return Question40()
        if qtype == 40:
            from .Question41 import Question41
            return Question41()
        if qtype == 41:
            from .Question42 import Question42
            return Question42()
        if qtype == 42:
            from .Question43 import Question43
            return Question43()
        if qtype == 43:
            from .Question44 import Question44
            return Question44()
        if qtype == 44:
            from .Question45 import Question45
            return Question45()
        if qtype == 45:
            from .Question46 import Question46
            return Question46()
        if qtype == 46:
            from .Question47 import Question47
            return Question47()
        if qtype == 47:
            from .Question48 import Question48
            return Question48()
        if qtype == 48:
            from .Question49 import Question49
            return Question49()
        if qtype == 49:
            from .Question50 import Question50
            return Question50()
        if qtype == 50:
            from .Question51 import Question51
            return Question51()
        if qtype == 51:
            from .Question52 import Question52
            return Question52()
        if qtype == 52:
            from .Question53 import Question53
            return Question53()
        if qtype == 53:
            from .Question54 import Question54
            return Question54()
        if qtype == 54:
            from .Question55 import Question55
            return Question55()
        if qtype == 55:
            from .Question56 import Question56
            return Question56()
        if qtype == 56:
            from .Question57 import Question57
            return Question57()
        if qtype == 57:
            from .Question58 import Question58
            return Question58()
        if qtype == 58:
            from .Question59 import Question59
            return Question59()
        if qtype == 59:
            from .Question60 import Question60
            return Question60()
        if qtype == 60:
            from .Question61 import Question61
            return Question61()
        if qtype == 61:
            from .Question62 import Question62
            return Question62()
        if qtype == 62:
            from .Question63 import Question63
            return Question63()
        if qtype == 63:
            from .Question64 import Question64
            return Question64()
        if qtype == 64:
            from .Question65 import Question65
            return Question65()
        if qtype == 65:
            from .Question66 import Question66
            return Question66()
        if qtype == 66:
            from .Question67 import Question67
            return Question67()
        if qtype == 67:
            from .Question68 import Question68
            return Question68()
        if qtype == 68:
            from .Question69 import Question69
            return Question69()
        if qtype == 69:
            from .Question70 import Question70
            return Question70()
        if qtype == 70:
            from .Question71 import Question71
            return Question71()
        if qtype == 71:
            from .Question72 import Question72
            return Question72()
        if qtype == 72:
            from .Question73 import Question73
            return Question73()
        if qtype == 73:
            from .Question74 import Question74
            return Question74()
        if qtype == 74:
            from .Question75 import Question75
            return Question75()
        if qtype == 75:
            from .Question76 import Question76
            return Question76()
        if qtype == 76:
            from .Question77 import Question77
            return Question77()
        if qtype == 77:
            from .Question78 import Question78
            return Question78()
        if qtype == 78:
            from .Question79 import Question79
            return Question79()
        if qtype == 79:
            from .Question80 import Question80
            return Question80()
        if qtype == 80:
            from .Question81 import Question81
            return Question81()
        if qtype == 81:
            from .Question82 import Question82
            return Question82()
        if qtype == 82:
            from .Question83 import Question83
            return Question83()
        if qtype == 83:
            from .Question84 import Question84
            return Question84()
        if qtype == 84:
            from .Question85 import Question85
            return Question85()
        if qtype == 85:
            from .Question86 import Question86
            return Question86()
        if qtype == 86:
            from .Question87 import Question87
            return Question87()
        if qtype == 87:
            from .Question88 import Question88
            return Question88()
        if qtype == 88:
            from .Question89 import Question89
            return Question89()
        if qtype == 89:
            from .Question90 import Question90
            return Question90()
        if qtype == 90:
            from .Question91 import Question91
            return Question91()
        if qtype == 91:
            from .Question92 import Question92
            return Question92()
        if qtype == 92:
            from .Question93 import Question93
            return Question93()
        if qtype == 93:
            from .Question94 import Question94
            return Question94()
        if qtype == 94:
            from .Question95 import Question95
            return Question95()
        if qtype == 95:
            from .Question96 import Question96
            return Question96()
        if qtype == 96:
            from .Question97 import Question97
            return Question97()
        if qtype == 97:
            from .Question98 import Question98
            return Question98()
        if qtype == 98:
            from .Question99 import Question99
            return Question99()
        if qtype == 99:
            from .Question100 import Question100
            return Question100()
        if qtype == 100:
            from .Question101 import Question101
            return Question101()
        if qtype == 101:
            from .Question102 import Question102
            return Question102()
        if qtype == 102:
            from .Question103 import Question103
            return Question103()
        if qtype == 103:
            from .Question104 import Question104
            return Question104()
        if qtype == 104:
            from .Question105 import Question105
            return Question105()
        if qtype == 105:
            from .Question106 import Question106
            return Question106()
        if qtype == 106:
            from .Question107 import Question107
            return Question107()
        if qtype == 107:
            from .Question108 import Question108
            return Question108()
        if qtype == 108:
            from .Question109 import Question109
            return Question109()
        if qtype == 109:
            from .Question110 import Question110
            return Question110()
        if qtype == 110:
            from .Question111 import Question111
            return Question111()
        if qtype == 111:
            from .Question112 import Question112
            return Question112()
        if qtype == 112:
            from .Question113 import Question113
            return Question113()
        if qtype == 113:
            from .Question114 import Question114
            return Question114()
        if qtype == 114:
            from .Question115 import Question115
            return Question115()
        if qtype == 115:
            from .Question116 import Question116
            return Question116()
        if qtype == 116:
            from .Question117 import Question117
            return Question117()
        if qtype == 117:
            from .Question118 import Question118
            return Question118()
        if qtype == 118:
            from .Question119 import Question119
            return Question119()
        if qtype == 119:
            from .Question120 import Question120
            return Question120()
        if qtype == 120:
            from .Question121 import Question121
            return Question121()
        if qtype == 121:
            from .Question122 import Question122
            return Question122()
        if qtype == 122:
            from .Question123 import Question123
            return Question123()
        if qtype == 123:
            from .Question124 import Question124
            return Question124()
        if qtype == 124:
            from .Question125 import Question125
            return Question125()
        if qtype == 125:
            from .Question126 import Question126
            return Question126()
        if qtype == 126:
            from .Question127 import Question127
            return Question127()
        if qtype == 127:
            from .Question128 import Question128
            return Question128()
