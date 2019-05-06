# %%
import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

# parameters
w0 = np.array([0, 1, 1])
t_end = 100

# lorenz equation
def lorenz(t, w, r=28, theta=10, b=8/3):
    x_dot = theta*(w[1] - w[0])
    y_dot = r*w[0] - w[1] - w[0]*w[2]
    z_dot = w[0]*w[1] - b*w[2]
    return np.array([x_dot, y_dot, z_dot]) 

# fourth-order Runge-Kutta method 
def rk4(func, t0, w0, t_end, n =10000):
    ts = np.zeros(n+1)
    ws = np.zeros((n+1, w0.size))
    ws[0] = w0
    ts[0] = t0
    h = (t_end-t0)/n
    for i in range(1, n+1):
        k1 = func(ts[i-1], ws[i-1])
        k2 = func(ts[i-1] + 0.5*h, ws[i-1] + 0.5*h*k1)
        k3 = func(ts[i-1] + 0.5*h, ws[i-1] + 0.5*h*k2)
        k4 = func(ts[i-1] + h, ws[i-1] + h*k3)
        ts[i] = ts[0] + i*h
        ws[i] = ws[i-1] + (k1 + 2*k2 + 2*k3 + k4)*h/6
    return ts, ws

ts, ws = rk4(lorenz, 0, w0, t_end)

fig =  plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(ws[:, 0], ws[:, 1], ws[:, 2], lw=0.5)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.show()
    