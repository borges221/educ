import log
import excep

x = 0
y = 0

def init(a, b):
    global x 
    global y 
    x = a
    y = b
    log.universal_logger((x,y), data_description = "Ввод данных")
        

def int_num():
    print('\nВведите число 1:')
    a = excep.check_int()
    print('Введите число 2:')
    b = excep.check_int()
    init (a, b)


def float_num():
    print('\nВведите число 1:')
    a = excep.check_float()
    print('Введите число 2:')
    b = excep.check_float()
    init (a, b)


def complex_num ():
    print('\nВведите действительную часть числа 1:')
    d_1 = excep.check_float()
    print('Введите мнимую часть числа 1:')
    m_1 = excep.check_float()
    a = complex(d_1, m_1)
    print('\nВведите действительную часть числа 2:')
    d_2 = excep.check_float()
    print('Введите мнимую часть числа 2: ')
    m_2 = excep.check_float()
    b = complex(d_2, m_2)
    init (a, b)
