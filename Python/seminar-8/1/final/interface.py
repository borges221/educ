import excep
import log
import books
import contacts


def repeat_menu ():
    print('\nХотите выполнить новую операцию?\n \
1 - Да\n \
2 - Нет')
    answer = excep.check_menu(3)
    if answer == 1:
        return main_menu()
    else:
        end_prog()


def empl_list():
    print ('Выберите пункт меню:\n 1 - Вывести перечень всех контрагентов\n 2 - Главное меню\n 3 - Выход')
    type_book_list = excep.check_menu(4)
    if type_book_list == 1:
        books.print_card_list()
        repeat_menu()
    elif type_book_list == 2:
        main_menu()
        log.universal_logger("Главное меню", data_description = "Переход")
    else:
        end_prog()


def create_book_list():
    print ('Выберите пункт меню:\n 1 - Создать новый справочник\n 2 - Главное меню\n 3 - Выход')
    type_create_book = excep.check_menu(4)
    if type_create_book == 1:
        books.create_book()
        repeat_menu()
    elif type_create_book == 2:
        main_menu()
        log.universal_logger("Главное меню", data_description = "Переход")
    else:
        end_prog()


def open_book():
    print ('Выберите пункт меню:\n 1 - Открыть справочник\n 2 - Главное меню\n 3 - Выход')
    type_book_list = excep.check_menu(4)
    if type_book_list == 1:
        books.open_books()
        repeat_menu()
    elif type_book_list == 2:
        main_menu()
        log.universal_logger("Главное меню", data_description = "Переход")
    else:
        end_prog()
        
        
def del_book_list():
    print ('Выберите пункт меню:\n 1 - Удалить справочник\n 2 - Главное меню\n 3 - Выход')
    type_del_book = excep.check_menu(4)
    if type_del_book == 1:
        if excep.check_file('list_book.csv'):
            with open('list_book.csv', 'r', encoding='utf-8') as file:
                for line in file:
                    print(line[:-5])
            file.close()
        books.del_book()
        repeat_menu()
    elif type_del_book == 2:
        main_menu()
        log.universal_logger("Главное меню", data_description = "Переход")
    else:
        end_prog()


def add_empl():
    print ('Выберите пункт меню:\n 1 - Выберите, в какой справочник внести данные\n 2 - Главное меню\n 3 - Выход')
    type_book_list = excep.check_menu(4)
    if type_book_list == 1:
        contacts.create_card(books.open_book_for_work())
        repeat_menu()
    elif type_book_list == 2:
        main_menu()
        log.universal_logger("Главное меню", data_description = "Переход")
    else:
        end_prog()


def find_cont():
    print ('Выберите пункт меню:\n 1 - Выбрать справочник\n 2 - Главное меню\n 3 - Выход')
    type_book_list = excep.check_menu(4)
    if type_book_list == 1:
        contacts.find_contact(books.open_book_for_work())
        repeat_menu()
    elif type_book_list == 2:
        main_menu()
        log.universal_logger("Главное меню", data_description = "Переход")
    else:
        end_prog()
        
        
def del_cont():
    print ('Выберите пункт меню:\n 1 - Выбрать справочник\n 2 - Главное меню\n 3 - Выход')
    type_book_list = excep.check_menu(4)
    if type_book_list == 1:
        contacts.del_contact(books.open_book_for_work())
        repeat_menu()
    elif type_book_list == 2:
        main_menu()
        log.universal_logger("Главное меню", data_description = "Переход")
    else:
        end_prog()


def update_cont():
    print ('Выберите пункт меню:\n 1 - Выбрать справочник\n 2 - Главное меню\n 3 - Выход')
    type_book_list = excep.check_menu(4)
    if type_book_list == 1:
        contacts.change_cont(books.open_book_for_work())
        repeat_menu()
    elif type_book_list == 2:
        main_menu()
        log.universal_logger("Главное меню", data_description = "Переход")
    else:
        end_prog()


def end_prog ():
    print('\nВыполнение программы завершено. Спасибо!')
    log.universal_logger("по команде пользователя", data_description = "Выход") 
    exit()


def main_menu():
    print('Какое действие Вы хотите выполнить?\n \
1 - Вывести перечень всех контрагентов\n 2 - Создать новый справочник\n \
3 - Открыть справочник\n 4 - Удалить справочник\n \
5 - Добавить сотрудника\n 6 - Поиск сотрудника\n 7 - Изменить запись сотрудника\n 8 - Удалить запись сотрудника\n 9 - Выход')

    type_main_menu = excep.check_menu(10)

    if type_main_menu == 1:
        return empl_list()
    elif type_main_menu == 2:
        return create_book_list()
    elif type_main_menu == 3:
        return open_book()
    elif type_main_menu == 4:
        return del_book_list()
    elif type_main_menu == 5:
        return add_empl()
    elif type_main_menu == 6:
        return find_cont()
    elif type_main_menu == 7:
        return update_cont()
    elif type_main_menu == 8:
        return del_cont()
    else:
        end_prog()
        
main_menu()