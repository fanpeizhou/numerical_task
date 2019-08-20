import numpy as np 
import matplotlib.pyplot as plt 

r = np.random.random(10000000)
v = np.sqrt(-2*np.log(r))
x = np.arange(0,5,0.01)
pv = x*np.exp(-x**2/2)

font1 = {'family' :  'normal','size'   : 16,}

plt.hist(v, 200, normed=1, label='numerical')
plt.plot(x, pv, '--', label='theoretical')
plt.legend(prop=font1)
plt.xlabel('v', font1)
plt.ylabel('P(v)', font1)
plt.show()