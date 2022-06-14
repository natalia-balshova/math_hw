import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

x = np.linspace(-5, 5, 100)
plt.plot(x, x ** 2 - 1)
plt.plot(x, (np.exp(x) + x - 1) / x)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()


def equations(p):
    x, y = p
    return (x ** 2 - 1 - y, (np.exp(x) + x * (1 - y) - 1))

x1, y1 = fsolve(equations, (2, 4))
x2, y2 = fsolve(equations, (-1, 1))

print (x1, y1)
print (x2, y2)