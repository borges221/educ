# Исследуйте функцию: f(x) = 2 * x ** 3 + 2 * x ** 2 - 18 * x -18

from sympy import *
from sympy.plotting import plot

init_printing()

x = Symbol('x')
f = 2 * x ** 3 + 2 * x ** 2 - 18 * x -18
a = plot(f, (x, -0.8, 5))

# Нули функции

solveset(f, x)

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
a = plot(f, (x, -1.5, 1.5))

# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0

m = [-oo, oo]

incr_list = []
decr_list = []
m[1:1] = solve(f, x)
for i in range(1, len(m)):
    boo = is_increasing(f, Interval.open(m[i-1], m[i]))
    if boo:
        incr_list.append(f'{m[i-1]}, {m[i]}')
    else:
        decr_list.append(f'{m[i-1]}, {m[i]}')

print("f > 0:", *incr_list, sep="\n")
print("f < 0:", *decr_list, sep="\n")