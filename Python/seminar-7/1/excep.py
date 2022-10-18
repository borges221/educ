import input_n
import interface
import log

def excep_check_zero():
    try:
        input_n.x / input_n.y
        return True
    except ZeroDivisionError:
        return False


def check_menu(quan):
    while True:
        try:
            ent_menu = (input())
            while int(ent_menu) not in range (1, quan):
                print ('\nНеверный ввод! Повторите ввод:')
                log.universal_logger("Неверный пункт меню", data_description = "Ошибка ввода") 
                ent_menu = (input())
            return int(ent_menu)
        except ValueError:
            print ('\nНеверный формат! Повторите ввод:')
            log.universal_logger("Неверный формат ввода меню", data_description = "Ошибка ввода")


def if_zero():
    print ('Ошибка! Деление на ноль. Повторите ввод данных')
    log.universal_logger("Деление на 0", data_description = "Ошибка")
    interface.menu_4()
    

def check_int():
    while True:
        try:
            enter_num = (input())
            return int(enter_num)
        except ValueError:
            print ('\nНеверный формат! Повторите ввод:')
            log.universal_logger("Неверный формат ввода данных", data_description = "Ошибка ввода")


def check_float():
    while True:
        try:
            enter_num = (input())
            return float(enter_num)
        except ValueError:
            print ('\nНеверный формат! Повторите ввод:')
            log.universal_logger("Неверный формат ввода данных", data_description = "Ошибка ввода")
