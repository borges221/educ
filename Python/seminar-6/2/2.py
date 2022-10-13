# Для чисел в пределах от 20 до N найти числа, 
# кратные 20 или 21.
#  Use comprehension.

print("enter the number")
def main(num):
    res_ls = [i for i in range(20, num+1) if i % 20 == 0 or i % 21 == 0]
    print(res_ls)


n = int(input())
main(n)
