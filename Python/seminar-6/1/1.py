# Представлен список чисел. 
# Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. 
# Use comprehension.

from random import sample


def randomMas(len: int):
    if len < 0:
        print("Negative value entered.")
        return []
    else:
        mas = sample(range(start, theend), len)
        return mas
print("Enter Range:")
start = int(input("From "))
theend = int(input("Till "))  

masiv = randomMas(int(input("Enter the number of numbers in the list: ")))
print(masiv)

new_masiv = [masiv[i] for i in range(1, len(masiv)) if masiv[i] > masiv[i - 1]]
print(new_masiv) 