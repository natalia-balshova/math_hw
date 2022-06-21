import numpy as np

k, n = 0, 10
p = []
for i in range(n):
    a = np.random.randint(0, 2)
    p.append(a)
    if a == 1:
        print('орел')
    else:
        print('решка')
    k += 1

p1 = p.count(1) / n
p2 = p.count(0) / n
print(f'Вероятность орла: {p1}')
print(f'Вероятность решки: {p2}')
print(f'Сумма вероятностей {p1 + p2}')


