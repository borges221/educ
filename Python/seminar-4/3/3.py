# Задайте последовательность чисел.
#  Напишите программу, 
#  которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.

from random import randint

number_of_elements = int(input('Enter the number of list items: '))

def get_array(number_of_elements):
    array = []
    for i in range(number_of_elements):
        array.append(randint(0, 9))
    return array

def find_non_repeating_elements(arr):
    res = []
    for i in arr:
        if arr.count(i) == 1:
            res.append(i)
    return res

if number_of_elements > 0:
    arr = get_array(number_of_elements)
    print(arr)
    print(find_non_repeating_elements(arr))
else:
    print('incorrect input')