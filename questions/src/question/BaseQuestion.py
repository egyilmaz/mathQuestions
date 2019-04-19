import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (0.01,0.01)
from io import BytesIO
import base64
from django.template import Template

class BaseQuestion:

    def meta(self):
        type_str=str(type(self))
        #"<class 'questions.src.question.Question1.Question1'>"  
        # becomes "Meta: question.Question1.Question1"
        return 'Meta: '+type_str[1:-2].split('.')[-1]+" "+str(self.type)+" "+str(self.complexity)

    def graphic(self):
        return None

    def answer(self):
        return None

    def answer_graphic(self):
        return None

    def context(self):
        text = self.question()
        graphic = self.graphic()
        meta = self.meta()
        answer = self.answer()
        answer_graphic = self.answer_graphic()
        return {"text": text, "graphic": graphic, "meta": meta, "answer": answer, "answer_graphic": answer_graphic}

    def template(self):
        template_str =  "<div>"\
                            "{{ text }}"\
                            "{% if graphic %}"\
                                "<div class=\"qi\"><img src=\"data:image/png;base64,{{graphic}}\"></div>"\
                            "{% endif %}"\
                            "<div >"\
                                "{% csrf_token %}"\
                                "<input type=\"text\" id=\"user_input\" placeholder=\"Type in your answer here\"><br>"\
                                "<input type=\"hidden\" id=\"correct_answer\" value=\"{{answer}}\" />"\
                                "<input type=\"hidden\" id=\"meta\" value=\"{{meta}}\" />"\
                                "<button onclick=\"EvalAndSubmit('{{qid}}')\">Check</button><br>"\
                                "<div id=\"hidden_answer_{{qid}}\" style=\"display:none;\">"\
                                    "{% if answer %}"\
                                        "<br>{{answer}}"\
                                    "{% endif %}"\
                                    "{% if answer_graphic %}"\
                                        "<div class=\"qi\"><img src=\"data:image/png;base64,{{answer_graphic}}\"></div>"\
                                    "{% endif %}"\
                                    "<br>{{meta}}"\
                                "</div><br>"\
                            "</div>"\
                        "</div>"
        return Template(template_str)

    def encode_graphics(self, a):
        plt.axis('off')
        plt.text(-1, 1, a, fontsize=11)
        buf = BytesIO()
        plt.savefig(buf, format='PNG', bbox_inches='tight', pad_inches=0)
        graphic = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n','')
        plt.clf()
        buf.close()
        return graphic
