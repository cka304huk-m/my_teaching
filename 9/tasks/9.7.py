# Победители Мировой серии.

def main():
    filename = 'WorldSeriesWinners.txt'

    # Сохраняю в переменую прочитаный файл.
    rf = read_file(filename)
    # Словарь с годами и победителями.
    yw = years_winners(rf)
    # Словарь с командами и кол-вом побед.
    cw = count_winners(yw)

    print('Введите год в диапазоне 1903 и 2009 годами.')
    year = input('Год: ')
    if year == '1904' or year == '1994':
        print('В', year, 'г. не проводили чемпионат.')
    elif year in yw:
        print('В этом году побеждала команда:', yw[year])
        comand = yw[year]
        print('У которой за сезон с 1903 - 2009 год -', cw[comand], 'побед(а/ы).')

def read_file(filename):
    """Читаю данные из файла"""

    with open(filename, 'r', encoding='utf-8') as rfile:

        winner = rfile.read().split('\n')

    rfile.close()

    return winner

def years_winners(filename):
    """Годы и команды побеждающие в них"""

    # Пустой словарь.
    com_win_year = {}

    # Перебираю список.
    for f in filename:
        # Если в списке есть значение: 1904
        # 1994 пропускаем их.
        if f[0:4] == '1904' or f[0:4] == '1994':
            continue
        else:
            # Записываем ключ(год):значение(команда)
            com_win_year[f[0:4]] = f[5:]

    # Возвращаю словарь.
    return com_win_year

def count_winners(dict_winner):
    """Команды и их победы с 1903 - 2009 г."""

    # Пустой словарь.
    com_win = {}

    # Перебираю словарь.
    for v in dict_winner.values():
        # Если в словаре нет значение, то записываю.
        if v not in com_win:
            # Записываю значение ключ(команда):значение(кол-во побед)
            com_win[v] = list(dict_winner.values()).count(v)

    # Возвращаю словарь.
    return com_win

main()