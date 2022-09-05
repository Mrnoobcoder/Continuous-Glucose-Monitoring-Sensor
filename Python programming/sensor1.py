import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
#Define Transfer function
num=np.array([1])

den=np.array([0,1])
den1=np.array([10,1])

den2=np.array([20,1])
H=signal.TransferFunction(num,den)
G=signal.TransferFunction(num,den1)
I=signal.TransferFunction(num,den2)

print('H(s)=',H)
#stemp respon
t,y=signal.step(H)
t,y1=signal.step(G)
t,y2=signal.step(I)
#plotting
plt.plot(t,y,'r',t,y1,'b',t,y2,'g')
plt.grid()
plt.show()
