import numpy as np
import plotly.express as px
def y(t):
    return (1/5)*np.exp(-t/5)
t=np.linspace(1,30)
fig=px.line(y(t),title='Impulse response')
fig.show()