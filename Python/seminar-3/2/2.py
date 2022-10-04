# Напишите программу, 
# которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.


from random import sample
from array import array
size = int(input("Enter size list "))

def multipDig(size):
    array = sample(range(1, 20), size)
    print(array)
    multip = 0
    count = 1
    lisnum = []
    if size % 2 == 0:
        for i in range(0, size // 2):
            multip = array[i] * array[-count]
            count += 1
            lisnum.append(multip) 
    else:
        for i in range(0, int(size / 2) + 1):
            multip = array[i] * array[-count]
            count += 1
            lisnum.append(multip)
    
    for k in range(size // 2):
        lisnum.append(array[k] * array[size - k - 1])
    print(lisnum)
    
multipDig(size)