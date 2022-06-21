# Дополните код расчетом коэффициента корреляции x и y по формуле

import numpy as np
import matplotlib.pyplot as plt

n = 100
r = 0.9
x = np.random.rand(n)
y = r * x + (1 - r) * np.random.rand(n)
plt.plot(x, y, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
c = np.corrcoef(x, y)
print(c)
a = (np.sum(x) * np.sum(y) - n * sum(x * y)) / (np.sum(x) ** 2 - n * np.sum(x ** 2))
b = (np.sum(y) - a * np.sum(x)) / n
print(np.mean(x))
print(np.mean(y))
r = np.sum((x-np.mean(x))*(y-np.mean(y))) / np.sqrt(np.sum((x-np.mean(x))**2) * np.sum((y-np.mean(y))**2))
print(r)
# A = np.vstack([x, np.ones(len(x))]).T
# a1, b1 = np.linalg.lstsq(A, y)[0]
plt.plot([0, 1], [b, a + b])
plt.show()
