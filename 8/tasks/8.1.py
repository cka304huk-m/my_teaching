# Инициалы. Напишите программу, которая получает
# строковое значение, содержащее имя, отчество и фамилию человека
# и показывает инициалы. Например, если пользователь
# вводит Михаил Иванович Кузнецов, то программа должна вывести М.И.К.

def main():
    """Основная функция."""
    first = input('Имя: ')
    last = input('Отчество: ')
    famaly = input('Фамилия: ')
    print(get_first_last_famaly(first, last, famaly))

def get_first_last_famaly(first, last, famaly):
    """Получает имя, отчество и фаилию человека
    и показывает инициалы."""
    set1 = first[0]
    set2 = last[0]
    set3 = famaly[0]

    initials = set1 + '.' + set2 + '.' + set3 + "."
    initials = initials.upper()

    return initials

# Вызываю основную функцию.
main()