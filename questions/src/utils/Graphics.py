import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def encode_image( plt ):
    buf = BytesIO()
    plt.savefig(buf, format='PNG', dpi=100)
    graphic = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n','')
    buf.close()
    return graphic

