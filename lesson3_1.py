# Напишите код на Python, реализующий расчет длины вектора, заданного его координатами.
import numpy as np

x = 13
y = 4
z = 7
len_vector = np.sqrt(x ** 2 + y ** 2 + z ** 2)
print(f'Длина векора ({x};{y};{z}) составляет {len_vector}')

# Способ 2
my_vector = np.array([13, 4, 7])
len_vector = np.linalg.norm(my_vector)
print(len_vector)
