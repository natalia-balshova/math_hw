import numpy as np
import matplotlib.pyplot as plt

x = []
x2 = []
y = []
y2 = []
for i in range(1001):
    a = 250
    b = 200
    x.append(i)
    x2.append(-i)
    y.append(np.sqrt(((i**2 / a**2)-1) * b**2))
    y2.append(-np.sqrt(((i**2 / a**2)-1) * b**2))

plt.plot(x, y, color='b')
plt.plot(x2, y, color='b')
plt.plot(x, y2, color='b')
plt.plot(x2, y2, color='b')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
