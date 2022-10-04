#  Напишите программу, которая принимает на вход 2 числа.
#  Получите значение N, 
# для пустого списка, 
# заполните числамив диапазоне [-N, N]. 
# Найдите произведение элементов на указанных позициях(не индексах).

n = int(input("Введите число N: "))
n1 = int(input("Position one: "))
n2 = int(input("Position two: "))

list = list(range(-n, n + 1))

print(list)
len = len(list)

if len >= n1 > 0 and len >= n2 > 0:
    print(list[n1 - 1] * list[n2 - 1])
else:
    print("Недопустимый индекс!")
