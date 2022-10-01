#  Напишите программу, 
#  которая принимает на вход цифру, 
#  обозначающую день недели,
#   и проверяет, 
#   является ли этот день выходным

numday = int(input("Ввдеите день недели"))
if numday > 0 and numday < 6:
    print("NO!")
elif numday == 6 or numday == 7:
    print("YES!!")
elif numday < 1 or numday > 7:
    print ("no such day of the week!")