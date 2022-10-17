import csv

def add_contact():
    name = input('Введите имя контакта: ')
    phone = input('Введите номер телефона: ')
    new_contact = [name, phone]
    with open(r'D:\-\Python\seminar-7\2\phonebook.csv', 'a', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(new_contact)

def delete_contact():
    name = input('Введите имя контакта для удаления: ')
    temp_list = []
    with open(r'D:\-\Python\seminar-7\2\phonebook.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            temp_list.append(row)
        for item in temp_list:
            if name in item:
                temp_list.remove(item)
                print('Запись удалена')
                break              
        with open(r'D:\-\Python\seminar-7\2\phonebook.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows(temp_list) 

def find_contact():
    name = input('Введите имя контакта для поиска: ')
    with open(r'D:\-\Python\seminar-7\2\phonebook.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if name == row[0]:
                print(*row)
        if name not in reader:
                print('Указанный контакт отсутствует.')

def show_all_contacts():
    with open(r'D:\-\Python\seminar-7\2\phonebook.csv', 'r') as file:
        reader = csv.reader(file)
        print('Ваши контакты: ')
        for row in reader:
            print('{:<10} {:<10}'.format(*row))