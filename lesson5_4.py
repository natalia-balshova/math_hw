# 4. (не обязательно, но желательно) Из урока по комбинаторике повторите расчеты,
# сгенерировав возможные варианты перестановок для других значений n и k

import numpy as np
import itertools

k = 0
for p in itertools.permutations('1234', 4):
    print(''.join(p))
    k += 1
print(f'Количество размещений: {k}')

k = 0
for p in itertools.combinations('1234', 4):
    print(''.join(p))
    k += 1
print(f'Количество сочетаний: {k}')
