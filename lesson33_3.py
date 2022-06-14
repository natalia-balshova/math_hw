# 3. Задание (в программе)
# Напишите код, который будет переводить полярные координаты в декартовы.
# Напишите код, который будет рисовать график окружности в полярных координатах.
# Напишите код, который будет рисовать график отрезка прямой линии в полярных координатах.
import math
import numpy as np
import matplotlib.pyplot as plt


def func_1(r, alpha):
    x = r * math.cos(alpha)
    y = r * math.sin(alpha)
    print(f'Декартовы координаты: ({x};{y}')


func_1(5, (math.pi / 6))        # полярные координаты в декартовы

a = np.arange(0., 2., 1./180.)*np.pi    # 360 точек
plt.polar(a, [10]*len(a))  # окружность

phi = np.arange(4, 8, 2)
rho = np.arange(4, 8, 2)
plt.polar(phi, rho)
plt.show()



