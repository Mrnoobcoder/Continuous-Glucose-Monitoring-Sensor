from tokenize import PlainToken
import numpy as np
import matplotlib.pyplot as plt 
def h(t):
    return (1/5)*np.exp(-t/5)
t=np.linspace(0,30)
plt.plot(t,h(t),color='red')
plt.show()