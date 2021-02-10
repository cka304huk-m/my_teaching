# Константы для строк и столбцов.
ROWS = 5
COLS = 3

def two_list():
    # Создаю 2х мерный список.
    two = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

    for r in range(ROWS):
        for c in range(COLS):
            two[r][c] = int(input('Число: '))

    return two

print(two_list())