import excep
import interface
import log


def list_of_data(num_ent):
    fill_list = {1: "фамилию", 2: "имя", 3: "отчество", 4: "номер телефона",
                  5: "дату вступления в должность в формате ДД.ММ.ГГГГ", 6: "должность"}
    return fill_list.get(num_ent)
    
    
def enter_data():
    card_list = []
    card_list.clear()
    count=0
    for i in range (1,6):
        temp = input(f'Введите {list_of_data(i)}:\n')
        if i == 4:
            while excep.check_phone(temp) is False:
                temp = input (f'Введите {list_of_data(i)}:\n')
            temp = ''.join([i for i in temp if i.isdigit()])
        elif i == 5:
            while excep.check_date(temp) is False:
                temp = input(f'Введите {list_of_data(i)}:\n')
        else:
            while excep.check_name_empl(temp) is False:
                print('Неверный ввод! Повторите ввод!')
                temp = input (f'Введите {list_of_data(i)}:\n')
            temp = temp.lower()
            temp = temp.capitalize()
        card_list.append(temp)
    print('Выберите должность:\n')
    with open('list_vac.csv', 'r', encoding='utf-8') as lst:
        for line in lst:
            print(f" {line}", end = '')
            count+=1
        print()
    lst.close()
    num_vac = excep.check_menu(count+1)
    with open('list_vac.csv', 'r', encoding='utf-8') as lst:
        for i, line in enumerate (lst):
            if i==num_vac-1:
                card_list.append(line.split('-')[1][1:])
    lst.close()
    return card_list
    

def create_card(empl_book):
    card = enter_data()
    with open(*empl_book, 'r', encoding='utf-8', newline='\n') as myfile:
        rd = myfile.readlines()
        ident = 0
        if rd:
            temp_for_num = (rd[-1].split(','))
            ident = temp_for_num[0]
        card.insert(0, int(ident)+1)
        myfile.close()
    with open(*empl_book, 'a', encoding='utf-8') as myfile:
        str_card = [str(a) for a in card]
        myfile.write(f'{",".join(str_card)}')
        print (f'Данные о контрагенте сохранены в справочнике!')
        log.universal_logger(f'{card[1]} {card[2]} {card[3]}', data_description = "Создан новый контрагент")
    



def find_contact(num_book):
    with open(*num_book, 'r', encoding='utf-8') as book:
        data = book.readlines()
    
    def search(data):        
        flag = 1
        name = input('Введите имя, фамилию, или номер телефона:\n')
        name = name.lower()
        name = name.capitalize()
        global count_find_cont
        count_find_cont = 0
        for line in data:               
            if name in line:
                flag = 0
                count_find_cont+=1
                print(f"\033[32m {line} \033[39m")
                temp_cont = line
                log.universal_logger(f'{name}, справочник {num_book}', data_description = "Найден контакт по запросу")
        if flag:
            print('Совпадений не найдено')
            temp_cont = ''
            log.universal_logger(name, data_description = "Поиск контрагента, совпадений не найдено")
        return temp_cont
    temp_cont = search(data)
    book.close()
    return temp_cont


def del_contact(num_book):
    print ('Данные какого контрагента вы хотите удалить?')
    cont_for_del = find_contact(num_book)
    if cont_for_del == '':
        interface.repeat_menu()
    if count_find_cont !=1:
        print (f'Найдено {count_find_cont} контрагентов! Уточните запрос!')
        log.universal_logger(cont_for_del, data_description = "Удаление не выполнено, неполный запрос")
        interface.repeat_menu()
    else:
        print ('Вы уверены?\n 1 - Да\n 2 - Нет')
        answer_del = excep.check_menu(3)
        if answer_del == 1:
            with open(*num_book, 'r', encoding='utf-8') as book:
                data = book.readlines()
            book.close()
            with open(*num_book, 'w', encoding='utf-8') as book:
                for line in data:
                    if cont_for_del != line:
                        book.write(line)
            log.universal_logger(cont_for_del, data_description = "Удаление контрагента")
            book.close()
        else:
            interface.repeat_menu()



def change_cont(num_book):
    list_for_changes = find_contact(num_book)
    if list_for_changes == '':
        interface.repeat_menu()
    if count_find_cont !=1:     
        print (f'Найдено {count_find_cont} контрагентов! Изменение бужет выполнено для последнего из списка. Продолжить?\n \
1 - Продолжить\n 2 - Уточнить запрос\n 3 - Выход')
        answer = excep.check_menu(4)
        if answer == 1:
            return_change_cont(list_for_changes, num_book)
        elif answer == 2:
            change_cont(num_book)
        else:
            interface.end_prog()
    else:
        return_change_cont(list_for_changes, num_book)


def return_change_cont(data_for_changes, num_book):
    user_id = input('Для подтверждения - введите id записи: ')
    while not user_id in data_for_changes.split(','):
        print (f'Неверный id записи!')
        user_id = input('Для подтверждения - введите id записи: ')
    else:
        print ('Какие данные желаете изменить?\n 1 - Фамилию\n 2 - Имя\n 3 - Отчество\n \
4 - Номер телефона\n 5 - Дату вступления в должность\n 6 - Должность\n 7 - Выход')
        choice_change = excep.check_menu(8)
        if choice_change == 7:
            interface.end_prog()
        temp_change = input(f"Введите {list_of_data(choice_change)}:\n")
        if choice_change in [1,2,3,6]:
            while excep.check_name_empl(temp_change) is False:
                print('Невернй ввод! Повторите ввод!')
                temp_change = input (f'Введите {list_of_data(choice_change)}:\n')
                temp_change = temp_change.lower()
                temp_change = temp_change.capitalize()
        elif choice_change == 4:
            while excep.check_phone(temp_change) is False:
                choice_change = excep.check_phone(input (f'Введите {list_of_data(choice_change)}:\n'))
        elif choice_change == 5:
            while excep.check_date is False:
                choice_change = excep.check_date(input (f'Введите {list_of_data(i)}:\n'))
        ident = ''
        with open(*num_book, 'r', encoding='utf-8') as book:
            data = book.readlines()
        book.close()
        with open(*num_book, 'w', encoding='utf-8') as myfile:
            for line in data:
                temp_list = line.split(',')
                ident = temp_list[0]
                if ident == user_id:
                    temp_list[choice_change] = temp_change
                    str_line = [str(a) for a in temp_list]
                    myfile.write(",".join(str_line))
                    print (f'Данные о контрагенте сохранены в справочнике!')
                else:
                    str_line = [str(a) for a in temp_list]
                    myfile.write(",".join(str_line))
        log.universal_logger(f"{data_for_changes[:-1]}, измененили - {list_of_data(choice_change)}", data_description = "Изменение данных пользователя")