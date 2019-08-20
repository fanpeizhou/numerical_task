import numpy as np
import matplotlib.pyplot as plt
from numba import jit
@jit

def p(x):
    px = np.exp(-(np.abs(x)**(5/3)))
    return px

num = 10000000
r1 = np.random.random(num)
x = -1 + 2*r1
r2 = np.random.random(num)
y = r2
f = []

for i in range(num):
    if y[i] < p(x[i]):
        f.append(x[i])

x = np.arange(-1,1,0.01)
font1 = {'family' :  'normal','size'   : 16,}

plt.hist(f, 200, normed=1, label='numerical')
plt.plot(x, 0.7*p(x), '--', label='theoretical')
plt.legend(prop=font1)
plt.xlabel('x', font1)
plt.ylabel('P(x)', font1)
plt.show()