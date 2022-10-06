# Задайте натуральное число N. 
# Напишите программу, 
# которая составит список простых множителей числа N.

n = int(input('Enter N: '))

def prime_factors_of_a_number(n):
    res = []
    while n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        if not n % 2:
            res.append(2)
            n /= 2
        elif not n % 3:
            res.append(3)
            n /= 3
        elif not n % 5:
            res.append(5)
            n /= 5
    if n > 1:        
        res.append(int(n))
    return res

print('List of prime factors of a number ', n, ' = ', prime_factors_of_a_number(n))