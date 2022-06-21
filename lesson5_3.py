import numpy as np
import math

k, n = 0, 1000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d
for i in range(0, n):
    if x[i] == 2:
        k = k + 1
# v = (0.5 ** k) * (0.5 ** (n - k))
print(k, n, k / n)
p = (math.factorial(n) / (math.factorial(k)*math.factorial(n - k))) * (0.5 ** k) * (0.5 ** (n - k))
print(p)
print()
n2 = 10     #испытаний
k2 = 3      #успех
p2 = (math.factorial(n2) / (math.factorial(k2)*math.factorial(n2 - k2))) * (0.5 ** k2) * (0.5 ** (n2 - k2))
print(p2)
