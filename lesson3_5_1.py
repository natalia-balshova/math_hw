import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
x = np.arange(-5, 5, 0.5)
y = np.arange(-5, 5, 0.5)
x, y = np.meshgrid(x, y)
z = 2 * x + 5 * y
z2 = 2 * x + 5 * y + 20
ax.plot_wireframe(x, y, z, colors='green')
ax.plot_wireframe(x, y, z2, colors='blue')
plt.show()

