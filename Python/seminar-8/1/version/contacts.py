import excep
import interface
import log
import csv

def list_of_data(num_ent):
    fill_list = {0: "фамилию", 1: "имя", 2: "отчество", 3: "номер телефона",
                  4: "дату вступления в должность", 5: "должность"}
    return fill_list.get(num_ent)
    
    
def enter_data():
    card_list = []
    card_list.clear()
    count=0
    for i in range (5):
        temp = input(f'Введите {list_of_data(i)}:\n')
        if i == 3:
            while excep.check_phone(temp) is False:
                temp = excep.check_phone(input (f'Введите {list_of_data(i)}:\n'))
        elif i == 4:
            while excep.check_date is False:
                temp = excep.check_date(input (f'Введите {list_of_data(i)}:\n'))
        else:
            while excep.check_name_empl(temp) is False:
                print('Невернй ввод! Повторите ввод!')
                temp = input (f'Введите {list_of_data(i)}:\n')
        card_list.append(temp)
    print('Выберите должность:\n')
    with open('list_vac.csv', 'r', encoding='utf8') as lst:
        for line in lst:
            print(f" {line}", end = '')
            count+=1
        print()
    lst.close()
    num_vac = excep.check_menu(count)
    with open('list_vac.csv', 'r', encoding='utf8') as lst:
        for i, line in enumerate (lst):
            if i==num_vac:
                card_list.append(line.split('-')[1][1:])
    lst.close()
    return card_list
    

def create_card(empl_book):
    card = enter_data()
    with open(*empl_book, 'r', encoding='utf8', newline='\n') as myfile:
        rd = myfile.readlines()
        ident = 0
        if rd:
            temp_for_num = list(rd[-1])
            ident = temp_for_num[0]
        card.insert(0, int(ident)+1)
        myfile.close()
    with open(*empl_book, 'a', encoding='utf8') as myfile:
        myfile.write(str(card))
        print (f'Данные о сотруднике сохранены в справочнике!')
        log.universal_logger(f'{card[1]} {card[2]} {card[3]}', data_description = "Создан новый сотрудник")
    


count_find_cont = 0    
def find_contact(num_book):
    with open(*num_book, 'r', encoding='utf-8') as book:
        data = book.readlines()
    
    def search(data):        
        flag = 1
        name = input('Введите имя, фамилию, или номер телефона:\n')
        global count_find_cont
        count_find_cont = 0
        for line in data:               
            if name in line:
                flag = 0
                count_find_cont+=1
                print(f"\033[32m {line} \033[39m")
                temp_cont = line
                log.universal_logger(name, data_description = "Поиск контакта")
        if flag:
            print('Совпадений не найдено')
            temp_cont = ''
            log.universal_logger(name, data_description = "Поиск контакта, совпадений не найдено")
        return temp_cont
    temp_cont = search(data)
    book.close()
    return temp_cont





def del_contact(num_book):
    print ('Какой контакт хотите удалить?')
    cont_for_del = find_contact(num_book)
    if cont_for_del == '':
        interface.main_menu()
    else:
        print ('Вы уверены?\n 1 - Да\n 2 - Нет')
        answer_del = excep.check_menu(3)
        if answer_del == 1:
            if count_find_cont == 1:
                with open(*num_book, 'r', encoding='utf-8') as book:
                    data = book.readlines()
                book.close()
                with open(*num_book, 'w', encoding='utf-8') as book:
                    for line in data:
                        if cont_for_del != line:
                            book.write(line)
                log.universal_logger(cont_for_del, data_description = "Удаление контакта")
                book.close()
            else:
                print (f'Найдено {count_find_cont} контактов! Уточните запрос!')
                log.universal_logger(cont_for_del, data_description = "Удаление не выполнено")
        else: interface.main_menu()