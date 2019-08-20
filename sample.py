import numpy as np
import matplotlib.pyplot as plt

def f(x):
    if x>-0.5*np.pi and x<0.5*np.pi:
        y = np.cos(x)**2
    else:
        y = 0
    return y

def p(x):
    y = np.exp(-x**2/(2*sigma**2))/(np.sqrt(2*np.pi)*sigma)
    return y

# num = 100000
# sigma = 0.7
# n1 = np.pi*np.random.random(num)-0.5*np.pi

# r1 = np.random.random(num)
# r2 = np.random.random(num)
# n2 = np.sqrt(-2*np.log(r1))*np.cos(2*np.pi*r2)*sigma

# x = np.arange(num)
# y1 = [f(n1[0])]
# y2 = [f(n2[0])/p(n2[0])]

for i in range(1, num):
    m1 = y1[-1]*i + f(n1[i])
    m2 = y2[-1]*i + f(n2[i])/p(n2[i])
    y1.append(m1/(i+1))
    y2.append(m2/(i+1))

# font1 = {'family': 'Times New Roman','size': 20}
# plt.semilogx(x, np.array(y1)*np.pi, label='π<f>n')
# plt.semilogx(x, y2, color='red', label='<f/p>n')
# plt.semilogx(x, [0.5*np.pi]*num, '--', color='black', label='π/2')
# plt.legend(prop=font1)
# plt.xlabel('n', font1)
# plt.ylabel('π<f>n <f/p>n', font1)
# plt.show()

# x = np.arange(-3, 3, 0.01)
# sigma = 0.7
# y1 = []
# y2 = []
# y3 = []

# for i in range(len(x)):
#     m1 = p(x[i])
#     y1.append(m1)

# for i in range(len(x)):
#     m2 = f(x[i])
#     y2.append(m2)

# for i in range(len(x)):
#     m3 = f(x[i])/p(x[i])
#     y3.append(m3)

# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.plot(x, y3)
# plt.show()