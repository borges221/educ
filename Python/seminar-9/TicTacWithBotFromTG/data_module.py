# Тут храним массив, который карта поля и нужные функции для обработки этого массива


win_patterns = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),
                (2, 5, 8), (0, 4, 8), (2, 4, 6))  # если в этих позициях
# стоят XXX или OOO,
# то кто-то выйграл