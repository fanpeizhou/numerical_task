import numpy as np
import matplotlib.pyplot as plt
import copy

def Ep_func(s):
    Ep =np.zeros(10) 
    for i in range(9):
        Ep[i] = 0.5*(s[i+1]-s[i]-1)**2 + 0.25*(s[i+1]-s[i]-1)**4
    Ep[9] = 0.5*(s[0]-s[9]+9)**2 + 0.25*(s[0]-s[9]+9)**4
    return Ep.sum()

def Ek_func(v):
    ek = (0.5*m*v**2).sum()
    return ek

def Force(s):
    f = np.zeros(10)
    for i in np.arange(1, 9, 1):
        f[i] = ((s[i+1]-s[i]-1)+(s[i+1]-s[i]-1)**3) - ((s[i]-s[i-1]-1)+(s[i]-s[i-1]-1)**3)
    f[0] = ((s[1]-s[0]-1)+(s[1]-s[0]-1)**3) - ((s[0]-s[9]+9)+(s[0]-s[9]+9)**3)
    f[9] = ((s[0]-s[9]+9)+(s[0]-s[9]+9)**3) - ((s[9]-s[8]-1)+(s[9]-s[8]-1)**3)
    return f

m = []
for i in range(10):
    m.append(1)
m = np.array(m)     
r = np.arange(0.5, 10, 1)
rv1 = np.random.random(10) - 0.5
rv2 = rv1 - np.sum(m*rv1)/(10*m)
v = rv2/np.sqrt(Ek_func(rv2))
rt = []
vt = []
kt = []
Et = []
p = []
p.append(np.sum(m*v))
rt.extend(r)
vt.extend(v)
kt.append(Ek_func(v))
Et.append(1)
step = 100000
dt = 0.01

for i in range(step):
    f_old = Force(r)
    r = r + dt*v + (0.5*dt**2)*(Force(r))/m
    v = v + 0.5*dt*(f_old + Force(r))/m
    p.append(np.sum(m*v))
    kt.append(Ek_func(v))
    Et.append((Ep_func(r)))
    rt.extend(r)
    vt.extend(v)

rt = np.array(rt).reshape(step+1,10)
vt = np.array(vt).reshape(step+1,10)
t = np.arange(0, (step+0.5)*dt, dt)
# plt.hist(Et, 100, normed=1)
# plt.plot(t, p, label='p')
# plt.plot(t, kt, label='Ek')
# plt.plot(t, Et, label='E')
# plt.legend()
# plt.xlabel('t')
# plt.show()
# plt.plot(t, rt[:,0])
# plt.plot(t, rt[:,1])
# plt.plot(t, rt[:,2])
# plt.plot(t, rt[:,3])
# plt.plot(t, rt[:,4])
# plt.plot(t, rt[:,5])
# plt.plot(t, rt[:,6])
# plt.plot(t, rt[:,7])
# plt.plot(t, rt[:,8])
# plt.plot(t, rt[:,9])
# plt.xlabel('t')
# plt.ylabel('ri')
# plt.show()
font1 = {'family' :  'normal','size'   : 16,}

def zhengtai(x, mu, sigma):
    y = np.exp(-(x-mu)**2/(2*sigma**2))/(np.sqrt(2*np.pi)*sigma)
    return y

x = np.arange(-1.2, 1.2, 0.01)

plt.hist(Et, 100, normed=1)
plt.show()

# print(np.mean(vt[:,0]),np.std(vt[:,0]))
# plt.hist(vt[:,0], 200, normed=1)
# plt.plot(x, zhengtai(x, np.mean(vt[:,0]), np.std(vt[:,0])), label='Normal')
# plt.xlabel('v1', font1)
# plt.ylabel('P(v1)', font1)
# plt.legend(prop=font1)
# print(np.var(vt[:,0]))
# print(np.mean(0.5*vt[:,0]**2))
# plt.show()

# plt.hist(vt[:,1], 200, normed=1)
# # plt.plot(x, zhengtai(x, np.mean(vt[:,1]), np.std(vt[:,1])), label='Normal')
# plt.xlabel('v2', font1)
# plt.ylabel('P(v2)', font1)
# plt.legend(prop=font1)
# plt.show()
# print(0.5*np.sum(vt[:,0]**2)/len(vt[:,0]))
# print(0.5*np.sqrt(2)*np.sum(vt[:,1]**2)/len(vt[:,1]))
