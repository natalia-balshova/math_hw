import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([2, 5, 1])
print(f'Ранг исходной матрицы = {np.linalg.matrix_rank(a)}')
print(f'Определитель исходной матрицы = {np.linalg.det(a)}') #определитель
# c = np.concatenate((a, b.T), axis=1) #выдает ValueError
c = np.column_stack((a, b))
print(c)
print(f'Ранг расширенной матрицы = {np.linalg.matrix_rank(c)}')
print('Ответ: Нет решений')
a1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b1 = np.array([0, 0, 0])
c1 = np.column_stack((a1, b1))
print(np.linalg.matrix_rank(c1))
x1 = np.linalg.lstsq(a1, b1, rcond=None)
print(x1)
