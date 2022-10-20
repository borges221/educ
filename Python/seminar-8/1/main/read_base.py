def read_data():
    with open('base.csv', 'r', encoding='utf-8') as file:
        for line in file:
            print(line)
        file.close()