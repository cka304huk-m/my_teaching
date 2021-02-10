def square_lo_shu():
    """Содержит квадрат магический квадрат Ло Шу."""

    square_shu = [[4, 9, 2],
                  [3, 5, 7],
                  [8, 1, 6]]

    return square_shu

def input_list():
    """Двумерный список"""

    # Пустой список.
    empty_list = [[4, 9, 2],
                  [3, 5, 7],
                  [8, 1, 6]]

    return empty_list

def check_list_magic_square(empty):
    """Получаю список в качестве аргумента
    и определяю является ли он магическим
    квадратом Ло Шу."""

    # импортирую список с квадратом Ло Шу.
    square_shu = square_lo_shu()

    if square_shu == empty:
        print('Ваш двумерный список похож на квадрат Ло Шу.')
    else:
        print('Ваш двумерный список не похож на квадрат Ло Шу')


check_list_magic_square(input_list())