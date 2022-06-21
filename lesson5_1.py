import numpy as np

n = int(input("Сколько жетонов приобрел игрок? "))      # 1 жетон = 1 попытка
for i in range(n):
    a = int(input("Ваше число? "))
    b = np.random.randint(0, 37)
    print(f"Выпало поле:{b}")
    if a == b:
        print("Победа")
    else:
        print(f"У вас осталось {(n - 1) - i} попыток")
        i += 1
