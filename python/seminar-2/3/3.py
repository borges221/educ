# Задайте список из n чисел, 
# заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

n= int(input("Введите число N"))
sum = 0
list = []

for i in range(1, n + 1):
    result = round((1 + 1 / i) ** i)
    list.append(result)
    sum += result

print(list)
print(sum)