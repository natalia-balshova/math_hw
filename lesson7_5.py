import numpy as np

a = np.array([1, 5, 0], float)
b = np.array([2, 8, 7], float)
c = np.array([7, 1.5, 3], float)
v = np.cross(a, b)
print(np.inner(v, c))
w = np.cross(b, c)
print(np.inner(w, a))
