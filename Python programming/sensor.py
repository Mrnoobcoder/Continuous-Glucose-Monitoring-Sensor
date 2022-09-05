from glob import glob1
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import control.matlab as control

G=control.tf([1],[0,1])
G1=control.tf([1],[5,1])
G2=control.tf([1],[10,1])
G3=control.tf([1],[15,1])
print(G,G1,G2,G3)
y,t=control.impulse(G)
y1,t=control.impulse(G1)
y2,t=control.impulse(G2)
y3,t=control.impulse(G3)
plt.subplot(2, 2, 1)
plt.plot(t,y,'black')
plt.subplot(2, 2, 2)
plt.plot(t,y1,'g')
plt.subplot(2, 2, 3)
plt.plot(t,y2,'b')
plt.subplot(2, 2, 4)
plt.plot(t,y3,'r')
plt.grid()
plt.show()