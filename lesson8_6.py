import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([2, 5, 11])
q, r = np.linalg.qr(a)

# print(a)
# print(b)
# print(r)
#
# print(np.dot(q, r))
# print(np.dot(np.transpose(q), q))
x = np.linalg.lstsq(a, b, rcond=None)
print(x)

r1 = r[:2, :2]
b1 = np.dot(np.transpose(q), b)[:2]
x1 = np.linalg.solve(r1, b1)
print(x1)
x2 = np.append(x1, 0)
print(x2)
x = np.array([1.25,  0.5, -0.25])
print(np.linalg.norm(x), np.linalg.norm(np.dot(a, x) - b))
