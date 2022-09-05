import numpy as np
import control
import matplotlib . pyplot as plt
# %% Generating Bode plot :
wb = 1 # Bandwidth [ rad / s ]
H = control . tf ([1] , [1/ wb , 1])
w0 = 0.1
w1 = 10
dw = 0.001
nw = int (( w1 - w0 )/ dw ) + 1 # Number of points of freq
w = np . linspace ( w0 , w1 , nw )
( mag , phase_rad , w ) = control . bode_plot (H , w )
# %% Plotting :
plt . close ( 'all')
plt . figure (1 , figsize =(12 , 9))
plt . subplot (2 , 1 , 1)
plt . plot ( np . log10 ( w ) , mag , 'blue')
# plt . xlabel ( ’ w [ rad / s ] ’)
plt . grid ()
plt . legend ( labels =( 'mag',))
plt . subplot (2 , 1 , 2)
plt . plot ( np . log10 ( w ) , phase_rad *180/ np . pi )
plt . xlabel ( ' w [ rad / s ] ')
plt . grid ()
plt . legend ( labels =( 'phase [ deg ] ' ))
# %% Generating pdf file of the plotting figure :
plt.show()
