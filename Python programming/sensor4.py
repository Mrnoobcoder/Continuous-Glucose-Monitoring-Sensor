from scipy import signal
import matplotlib.pyplot as plt
sys=([1],[5,1])
t,y=signal.impulse(sys)
plt.plot(t,y)
plt.show()