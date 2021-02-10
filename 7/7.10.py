def main():
    # Основная функция.

    # Получаю список с командами победителями.
    wSw = get_file_winners()
    command, count = get_name_command(wSw)
    print(command, 'выигрывала', count, 'раз за 106 лет.')


def get_file_winners():
    """Читаю файл который сохраняю пустой список"""

    # Список куда буду сохранять данные из файла.
    wSw = []

    # Читаю файл.
    with open('WorldSeriesWinners.txt', 'r') as worldWiners:

        # Прохожу файл циклом и записываю данные в список,
        # при этом удаляю символ новой строки.
        for winers in worldWiners:
            wSw.append(winers.rstrip("\n"))

    # Закрываю файл.
    worldWiners.close()

    # Возвращаю список.
    return wSw

def get_name_command(winers):
    """Название команды, которое запрашиваю у пользователя."""

    name_command = input('Название команды: ')

    count = winers.count(name_command)
    return name_command, count

# Вызываю основную функцию.
main()