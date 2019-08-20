import numpy as np
import matplotlib.pyplot as plt
import copy
from numba import jit
@jit

def Hamiton(grid):
    H = 0
    for i in range(size):
        for j in range(size-1):
            H += grid[i, j]*grid[i, j+1]
        H += grid[i, 0]*grid[i, size-1]
    for i in range(size):
        for j in range(size-1):
            H += grid[j, i]*grid[j+1, i]
        H += grid[0, i]*grid[size-1, i]
    return -1*H

def p_reverse(H):
    p = np.exp(-H/(kb*T))
    return p 

def MC_step(grid):
    for i in range(size**2):
        grid_tem = copy.deepcopy(grid)
        grid[np.random.randint(size), np.random.randint(size)] *= -1
        if p_reverse(Hamiton(grid)-Hamiton(grid_tem)) < np.float(np.random.random(1)):
            grid = grid_tem
    return grid

size = 30
grid = np.full(np.zeros((size, size)).shape, -1)
kb = 1
T = 2.25
m_sum = [-1]
step = 10000
a = 100  # 舍去前面多少步

for i in range(step):
    grid = MC_step(grid)
    m_sum.append(grid.sum()/size**2)

m_sample = m_sum[-(step-a)::3]
m_average = [m_sample[0]]

for i in range(1, len(m_sample)):
    m1 = m_average[-1]*i + m_sample[i]
    m_average.append(m1/(i+1))

# x = np.arange(1, 4, 0.1)
# y = []
# for t in np.arange(1, 4, 0.1):
#     T = t
#     m_sum = [-1]
#     grid = np.full(np.zeros((size, size)).shape, -1)
#     for i in range(step):
#         grid = MC_step(grid)
#         m_sum.append(grid.sum()/size**2)
#     m_sample = m_sum[-(step-a)::3]
#     m_average = [m_sample[0]]
#     for i in range(1, len(m_sample)):
#         m1 = m_average[-1]*i + m_sample[i]
#         m_average.append(m1/(i+1))
#     y.append(m_average[-1])

font1 = { 'style':'italic', 'size': 20}
font2 = { 'size': 10}


# plt.plot(x, y, '.-', label='m')
# plt.plot(x, [0]*len(x), 'r--', label='0')
# plt.xlabel('T', font1)
# plt.ylabel('m', font1)
# plt.legend(prop=font2)
# plt.show()


x = np.arange(0, step+1, 1)
plt.matshow(grid)
plt.show()
plt.plot(x, m_sum, '.-', label='m')
plt.plot(x, [0]*(step+1), 'r--', label='0')
plt.plot(x[-(step-a)::3], m_average, '-', label='m_average')
plt.xlabel('MC_step', font1)
plt.ylabel('m', font1)
plt.legend(prop=font2)
plt.show()
# print(m_average[-1])