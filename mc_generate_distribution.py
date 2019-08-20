import numpy as np
import matplotlib.pyplot as plt
from numba import jit
@jit

def p(x):
    if x>-0.5*np.pi and x<0.5*np.pi:
        y = np.cos(x)**2
    else:
        y = 0
    return y

x = -1
px = [x]
# sigma = 1
# def p(x):
#     y = np.exp(-x**2/(2*sigma**2))/(np.sqrt(2*np.pi)*sigma)
#     return y
# metropolis method
for i in range(10000000):
    x1 = x
    p1 = p(x1)
    x = x + np.float(np.random.random(1)) - 0.5
    p2 = p(x)
    if p2 >= p1:
        px.append(x)
    if p2 < p1: 
        if np.float(np.random.random(1)) < p2/p1:
            px.append(x)
        else:
            x = x1
            px.append(x1)

x = np.arange(-2, 2, 0.01)
fx = []
for i in range(len(x)):
    fx.append(p(x[i]))

font1 = {'family' :  'normal','size'   : 16,}
font2 = {'family' :  'normal','size'   : 12,}
n, bins, patches = plt.hist(px, 200, normed=1, label='MC')
# plt.show()
plt.semilogy(x, 2*np.array(fx)/np.pi, '--', label='2cos(x)^2/π')
plt.legend(prop=font2)
plt.xlabel('x', font1)
plt.ylabel('P(x)', font1)
plt.ylim(0.000001, 10)
plt.show()
# semilogy
# plt.scatter(range(100), px[:100])
# plt.show()







# ppx=[]
# inn = np.random.randint(10000, size = 1000)
# for i in inn:
#     ppx.append(px[i])

# plt.hist(ppx, 100)
# plt.show()