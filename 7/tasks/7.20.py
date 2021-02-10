def main():
    # Глобальные константы.
    ROWS = 3
    COLS = 4

    # Создаю 2х мерный список
    values = [[2, 2, 0, 60],
              [0, 1, 3, 0],
              [0, 4, 0, 7]]
    print(values)

    for r in range(ROWS):
        for c in range(COLS):
            values[r][c] = 0

    print(values)

main()