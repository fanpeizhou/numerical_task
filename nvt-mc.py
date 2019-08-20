import numpy as np
import matplotlib.pyplot as plt
import copy

def Ep_func(s):
    Ep =np.zeros(10) 
    for i in range(9):
        Ep[i] = 0.5*(s[i+1]-s[i]-1)**2 + 0.25*(s[i+1]-s[i]-1)**4
    Ep[9] = 0.5*(s[0]-s[9]+9)**2 + 0.25*(s[0]-s[9]+9)**4
    return Ep.sum()

def delta_U(Ep_new, Ep_old):
    deltau = np.exp(-(Ep_new-Ep_old)/(kb*T))
    return deltau 

def mc(r, ep):
    for n in range(num):
        r_tem = copy.deepcopy(r)
        r[np.random.randint(10)] += 2*step*(np.float(np.random.random(1))-0.5)
        if Ep_func(r)-Ep_func(r_tem) <= 0:
            r_sum.extend(r)
            ep.append(Ep_func(r))
        if Ep_func(r)-Ep_func(r_tem) > 0:
            if delta_U(Ep_func(r), Ep_func(r_tem)) > np.float(np.random.random(1)):
                r_sum.extend(r)
                ep.append(Ep_func(r))
            else:
                r = r_tem
                r_sum.extend(r_tem)
                ep.append(Ep_func(r_tem))
    return ep

# r = np.arange(0.5, 10, 1)
# r_sum = []
# r_sum.extend(r)
kb = 1.381*10**(-23)
t = 0.1*10**22
step = 0.3
num = 100000
# ep = [0]
y = []
x = []

for i in range(1, 100, 5):
    r = np.arange(0.5, 10, 1)
    r_sum = []
    r_sum.extend(r)
    ep = [0]
    T = i*t
    ep_mean = np.mean(mc(r, ep))
    x.append(i)
    y.append(ep_mean)
    
plt.plot(x, y, '.--')  
plt.show()








# r_sum = np.array(r_sum).reshape(num+1,10)
# t = np.arange(0, num+1, 1)
# plt.plot(t, r_sum[:,0])
# plt.plot(t, r_sum[:,1])
# plt.plot(t, r_sum[:,2])
# plt.plot(t, r_sum[:,3])
# plt.plot(t, r_sum[:,4])
# plt.plot(t, r_sum[:,5])
# plt.plot(t, r_sum[:,6])
# plt.plot(t, r_sum[:,7])
# plt.plot(t, r_sum[:,8])
# plt.plot(t, r_sum[:,9])
# plt.xlabel('t')
# plt.ylabel('ri')
# plt.show()

# def zhengtai(x, a):
#     y = 0.5*a**3*(x**2)*np.exp(-a*x)     #+(1/3)*a**5*(1/24)*(x**4)*np.exp(-a*x)
#     return y

# x = np.arange(0, 3, 0.01)

# plt.hist(ep[-90000:], 100, normed=1)
# plt.plot(x, zhengtai(np.array(x), 1/(kb*T)))
# plt.show()

# print(np.mean(ep[-90000:]))
# print(np.var(np.array(ep[-90000:])))
