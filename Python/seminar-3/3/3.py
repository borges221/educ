# ;  Напишите программу, 
# ;  которая будет преобразовывать десятичное число в двоичное.
# ; Без использования встроенной функции преобразования, 
# ; без строк.
# ; Без использования встроенной функции преобразования, 
# ; без строк.

Num = int(input("Введите число: "))

def binary(Num):
    number = []
    while Num:
        binnar = Num % 2
        Num //= 2
        number.append(binnar)
    number.reverse()
    result = int("".join(map(str, number)))
    print(result)

binary(Num)