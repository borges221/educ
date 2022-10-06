# Вычислить число c заданной точностью d

from decimal import Decimal, getcontext 

num = Decimal(input('Enret number: '))
accuracy = str(input('mask rounding precision"0.001": '))

def rounding_accuracy(user_number, accuracy):
    getcontext().prec = len(accuracy) - 1
    user_number = user_number * (10**len(accuracy)-1) / (10**len(accuracy)-1)
    return user_number

print(rounding_accuracy(num, accuracy))