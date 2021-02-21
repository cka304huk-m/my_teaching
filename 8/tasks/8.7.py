# Анализ символов.
def main():
    """Оносвная функция."""
    filename = 'text.txt'
    my_string = read_file(filename)
    l_upeer, l_lower, num, space = count_symbols(my_string)
    print('Количество символов:')
    print('В верхнем регистре -', l_upeer)
    print('В нижнем регистре -', l_lower)
    print('Цифр -', num)
    print('Пробелов -', space)

def read_file(filename):
    """Читает данные из фала в строку и возвращает её."""

    # Строка для сохрания всего файла.
    my_string = ''

    # Читаю данные.
    with open(filename, 'r') as fread:

        # Перебираю файл.
        for r in fread:
            # Сохраняю перебраные данные в строку.
            my_string += r

    # Закрываю файл.
    fread.close()

    # Возвращаю строку.
    return my_string

def count_symbols(my_string):
    """Считаю:
    • количество букв в файле в верхнем регистре;
    • количество букв в файле в нижнем регистре;
    • количество цифр в файле;
    • количество пробельных символов в файле.
    """

    # Переменные счетчики.
    count_litters_upper = 0
    count_litters_lower = 0
    count_num = 0
    count_space = 0

    # Перебираю строку.
    for s in my_string:
        if s.isupper():
            count_litters_upper += 1
        elif s.islower():
            count_litters_lower += 1
        elif s.isdigit():
            count_num += 1
        elif s.isspace():
            count_space += 1

    return count_litters_upper, count_litters_lower, count_num, count_space

# Вызываю основную функцию.
main()