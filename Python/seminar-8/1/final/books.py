import os
import excep
import log
import interface


def create_book():
    name = input('Введите имя нового справочника:\n')
    res_check_name = excep.check_name_file(name)
    while res_check_name is False:
        name = input('Повторите ввод:\n')
        res_check_name = excep.check_name_file(name)
    else:
        if excep.os.path.isfile(name) is True:
            print("Справочник уже существует!")
            log.universal_logger(name, data_description = "Ошибка создания справочника, справочник уже существует")
        else:
            with open ('list_book.csv','a', encoding='utf-8', newline='') as list_book:
                list_book.write(f'{name}.csv\n')
            with open(f'{name}.csv', 'a', encoding='utf-8') as new_book:
                new_book.write('')
                print (f'Справочник "{name}" успешно создан!')
                log.universal_logger(name, data_description = "Создание справочника")
            new_book.close()


def del_book():
    if excep.check_file('list_book.csv') is False:
        print(f'Системная ошибка! Справочники отсутствуют!')
        log.universal_logger("Справочники отсутсвуют в базе", data_description = "Ошибка удаления справочника")
        interface.repeat_menu()
    name = input('Какой справочник желаете удалить? Введите название:\n')
    res_check_name = excep.check_name_file(name)
    while res_check_name is False:
        name = input('Повторите ввод:\n')
        res_check_name = excep.check_name_file(name)
    if excep.os.path.isfile(f'{name}.csv'):
        print ('Вы уверены?\n 1 - Да\n 2 - Нет')
        answer_del = excep.check_menu(3)
        if answer_del == 1:
            os.remove(f'{name}.csv')
            print(f"Справочник {name} успешно удален!")
            log.universal_logger(name, data_description = "Удаление справочника")
            with open ('list_book.csv', 'r', encoding='utf-8') as list_b:
                lines = list_b.readlines()
            list_b.close()
            with open ('list_book.csv', 'w', encoding='utf-8') as list_b:
                for line in lines:
                    if line!=name+".csv\n":
                        list_b.write(line)
            list_b.close
        elif answer_del == 2:
            interface.repeat_menu()
    else:
        print("Такого справочника не существует!")
        log.universal_logger(name, data_description = "Ошибка удаления справочника, справочник отуствует в базе")


def print_card_list():
        if excep.check_file('list_book.csv'):
            with open('list_book.csv', 'r', encoding='utf-8') as file:
                for line in file:
                    print (f'\nСправочник "{line[:-5]}"\n')
                    with open(line[:-1], 'r', encoding='utf-8') as temp_file:
                        for temp_line in temp_file:
                            print(temp_line, end="")
                    temp_file.close()
            file.close()
            log.universal_logger('Перечень контрагентов', data_description = "Запрос")
        else:
            print(f'Системная ошибка! Данные о контрагентах отсутствуют!')
            log.universal_logger("Справочники отсутсвуют в базе", data_description = "Ошибка запроса перечня контрагентов")


def open_books():
    if excep.check_file('list_book.csv') is False:
        print(f'Системная ошибка! Справочники отсутствуют!')
        log.universal_logger("Справочник отуствует в базе", data_description = "Ошибка чтиения справочника")
        interface.repeat_menu()
    else:
        print ('Какой справочник желаете открыть?')
        temp_dict = {}
        temp_dict.clear()
        count = 1
    with open ('list_book.csv', 'r', encoding='utf-8') as file:
        for line in file:
            print(f'{count} - Cправочник "{line[:-5]}"')
            temp_dict[count] = line.split()
            count += 1
    file.close()
    num_book = excep.check_menu(count)
    with open(*temp_dict[num_book],'r', encoding='utf-8') as open_file:
        for line in open_file:
            print(line, end ='')
    open_file.close()
    log.universal_logger(f'Открытие справочника {temp_dict[num_book]}', data_description = "Запрос")
    return temp_dict[num_book]
  
    
def open_book_for_work():
    if excep.check_file('list_book.csv') is False:
        print(f'Системная ошибка! Справочники отсутствуют!')
        log.universal_logger("Справочник отуствует в базе", data_description = "Ошибка чтения справочника")
        interface.repeat_menu()
    print ('Какой справочник хотите использовать?')
    with open('list_book.csv', 'r', encoding='utf-8') as file:
        temp_dict = {}
        temp_dict.clear()
        count = 1
        for line in file:
            print(f'{count} - Cправочник {line[:-5]}\n', end='')
            temp_dict[count] = line.split()
            count += 1
    file.close()
    num_book = excep.check_menu(count)
    return temp_dict[num_book]