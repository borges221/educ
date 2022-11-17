# -*- coding: utf-8 -*-

# -- Editor --

# Исследуйте функции:
# f = (x ** 2 + 3) / (3 * (x + 1))
from sympy import *

# from sympy.abc import x, y, f, g
# from sympy import Symbol, sin, cos

from sympy.plotting import plot

init_printing()

x = Symbol('x')
f = (x ** 2 + 3) / (3 * (x + 1))
a = plot(f, (x, -0.5, 0.5))

# Нули функции
solveset(f, x,)

# Найти интервалы
b = [-oo, oo]
b[1:1] = solve(diff(f), x)
b

# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
c = []
d = []
for i in range(1, len(b)):
    boo = is_increasing(f, Interval.open(b[i-1], b[i]))
    if boo:
        c.append(f"{b[i-1]} {b[i]}")
    else:
        d.append(f"{b[i-1]} {b[i]}")
print('Возрастает в диапазоне', c)
print('Убывает в диапазоне', d)

# 5. Вычислить вершину
# Экстремумы функции
e = solve(diff(f), x)
for i in e:
    g = f.subs(x, i)
    if g < 0:
        print(f'Нижний экстремум: x:{i} y:{g}')
    elif g > 0:
        print(f'Верхний экстремум: x:{i} y:{g}')
a = plot(f, (x, -0.5, 0.5))

