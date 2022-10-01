# Реализуйте алгоритм перемешивания списка.
#  Без функции shuffle из модуля random.

from random import randrange

n = int(input())
list = list(range(n))
len= len(list)

print(list)

for i in range(len):
    n1 = randrange(len)
    n2 = randrange(len)
    list[n1], list[n2] = list[n2], list[n1]

print(list)
