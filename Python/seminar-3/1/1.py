#  Задайте список, 
#  состоящий из произвольных чисел, 
#  количество задаёт пользователь.
# Напишите программу, 
# которая найдёт сумму элементов списка, 
# стоящих на нечётных позициях(не индексах).

from random import sample

size = int(input("Enter size list: "))

def sumDigOdd(size):
    array = sample(range(0, 100), size)
    print(array)
    sum = 0
    for i in range(0, size, 2):
        sum += array[i]
    print(f"Sum of list elements at odd positions = {sum}")

sumDigOdd(size)