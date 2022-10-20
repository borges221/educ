def create_card():
    with open('base.csv', 'a', encoding='utf-8') as file:
        file.write('{card_list}\n')