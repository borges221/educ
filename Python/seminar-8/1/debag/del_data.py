import csv

def del_data():
    name = input('Введите: ')
    temp = []
    with open(r'base.csv', 'r') as file:
        read = csv.reader(file)
        for row in read:
            temp.append(row)
        for item in temp:
            if name in item:
                temp.remove(item)
                print('Запись удалена')
                break              
        with open(r'base.csv') as file:
            writer = csv.writer(file)
            writer.writerows(temp)