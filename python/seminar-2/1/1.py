#  Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 

num = float(input("Введите число"))
sum = 0

power = len(str(num)) - 2
num *= 10 ** power

while num:
    sum += num % 10
    num //= 10
print ("Сумма ровна")
print(int(sum))
