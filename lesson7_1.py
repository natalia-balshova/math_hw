import numpy as np

a = np.array([1, 2, 3, 4])
b = np.arange(5, 9).reshape(1, 4) #другой способ создания вектора
print(a)
print(b)
k = 2
l = 3
#1
print((k * l) * a)
print(k * (a * l))
#2
print(k * (a + b))
print(k * a + k * b)
#3
print((k + l) * a)
print(k * a + l * a)
#4
c = np.array([2, 2, 2, 2])
# c.shape = -1, 1
print(np.dot(a+b, c))
print(np.dot(a, c) + np.dot(b, c))
# проверка 2й части
e = np.identity(5)
print(e)
p = 5 * e
print(p)
q = np.linalg.inv(p)
print(q)
print(np.dot(p, q))
