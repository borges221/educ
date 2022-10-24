import os
from datetime import datetime


def check_menu(quan):
    while True:
        try:
            ent_menu = (input())
            while int(ent_menu) not in range (1, quan):
                print ('\nНеверный ввод! Повторите ввод:')
                ent_menu = (input())
            return int(ent_menu)
        except ValueError:
            print ('\nНеверный формат! Повторите ввод:')


def check_file(name_file):
    if os.path.exists(name_file):
        if os.path.getsize(name_file)>0:
            return True
        else:
            return False
    else:
        return False


def check_name_file(ent_name):
    list_name = list(ent_name)
    error_pop = ['/','|','*','?','>','<',':','"','\\']
    for i in list_name:
        if i in error_pop or len(ent_name)<3:
            print ("Недопустимое название")
            return False
    return True


def check_phone (phone_data):
    num_for_write = ''.join([i for i in phone_data if i.isdigit()])
    if len(num_for_write) > 3:
        return True
    else:
        print ("Неверный формат!")
        return False

        
def check_name_empl (name_cont):
    if name_cont.isalpha() and len(name_cont)>1:
        return True
    else:
        return False


def check_date(date_text):
    try:
        bool(datetime.strptime(date_text, '%d.%m.%Y'))
    except ValueError:
        print ("Неверный формат!")
        return False