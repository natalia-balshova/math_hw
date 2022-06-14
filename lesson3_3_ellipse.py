import numpy as np
import matplotlib.pyplot as plt

x = []
x2 = []
y = []
y2 = []
for i in range(1001):
    a = 1000
    b = 300
    x.append(i)
    x2.append(-i)
    y.append(np.sqrt((1-(i**2 / a**2)) * b**2))
    y2.append(-np.sqrt((1-(i**2 / a**2)) * b**2))

plt.plot(x, y, color='g')
plt.plot(x2, y, color='g')
plt.plot(x, y2, color='g')
plt.plot(x2, y2, color='g')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
