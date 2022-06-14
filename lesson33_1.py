#Нарисуйте график функции:   для некоторых (2-3 различных) значений параметров k, a, b

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5*np.pi, 5*np.pi, 201)
k1 = 2
k2 = 4
k3 = 0.5
a1 = 2
a2 = 3
a3 = 1
b1 = 2
b2 = -2
b3 = 3
plt.plot(x, k1 * np.cos(x - a1) + b1)
plt.plot(x, k2 * np.cos(x - a2) + b2)
plt.plot(x, k3 * np.cos(x - a3) + b3)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

