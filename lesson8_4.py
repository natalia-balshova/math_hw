import numpy as np
import scipy.linalg

a = np.array([[1, 2, 3], [2, 16, 21], [4, 28, 73]])
p, l, u = scipy.linalg.lu(a)
print(p)
print(l)
print(u)