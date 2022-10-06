# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, 
# записать в файл полученный многочлен не менее 3-х раз.

import random
my_f = open("res.txt", "a+")
k = int(input("Enter number:   "))
lst = [random.randint(0,10) for i in range(k + 1)]
# print(lst)
x = ""
for i in range(k + 1):
    if i < k:
        x += str(lst[i]) + "*x^" + str(k-i)  +  " + " 
    else:
        x += str(lst[i] ) + " = 0"


my_f.write(f'{x}  \n')
my_f.close()