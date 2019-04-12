import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (0.01,0.01)
from io import BytesIO
import base64

class BaseQuestion:

    def meta(self):
        type_str=str(type(self))
        #"<class 'questions.src.question.Question1.Question1'>"  
        # becomes "Meta: question.Question1.Question1"
        return 'Meta: '+'.'.join(type_str[1:-2].split('.')[-3:])

    def graphic(self):
        return None

    def encode_graphics(self, a):
        plt.axis('off')
        plt.text(-1, 1, a, fontsize=11)
        buf = BytesIO()
        plt.savefig(buf, format='PNG', bbox_inches='tight', pad_inches=0)
        graphic = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n','')
        plt.clf()
        buf.close()
        return graphic

