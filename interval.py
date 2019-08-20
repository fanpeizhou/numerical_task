import numpy as np
import matplotlib.pyplot as plt

num = 100000
a = num*(np.sort(np.random.random(num)))
b = []

for i in range(num-1):
    interval = a[i+1] - a[i]
    b.append(interval)

n, bins, patches = plt.hist(b, 10, normed=1)
plt.show()
plt.plot(bins[:-1], np.log(n))
plt.show()
# print(n)
# print(patches)
# print(bins)