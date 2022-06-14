import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
x = np.arange(-100, 100, 0.5)
y = np.arange(-100, 100, 0.5)
x, y = np.meshgrid(x, y)
z = x**2 + y**2 #эллиптический параболоид
z2 = x**2 - y**2 #гиперболический параболоид
ax.plot_wireframe(x, y, z, colors='green')
ax.plot_wireframe(x, y, z2, colors='blue')
plt.show()