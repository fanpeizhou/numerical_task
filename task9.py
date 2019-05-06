import numpy as np
import matplotlib.pyplot as plt

num = 10000000
a = num*(np.sort(np.random.random(num)))
b = []

for i in range(num-1):
    interval = a[i+1] - a[i]
    b.append(interval)

plt.hist(b, 200, normed=1)
plt.show()