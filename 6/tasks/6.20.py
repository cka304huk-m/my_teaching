def main():
    # Основная функция.
    print("""
    МЕНЮ:
    1 - Записать данные в файл.
    2 - Прочитать данные из файла.
    """)
    choice = int(input('Ваш выбор - '))
    if choice == 1:
        write_golf()
    elif choice == 2:
        read_golf()
    else:
        print('Нет такого пункта в меню.')

def write_golf():
    # Записывает достижения игрока в файл golf.txt.

    # Открываю файл golf.txt в режим записи.
    golf = open('golf.txt', 'w')

    more = 'y'

    while more != 'n':
        name = input('Имя игрока: ')
        points = int(input('Заработал очков: '))
        # Записываю эти данные в файл.
        golf.write(name + "\n")
        golf.write(str(points) + "\n")

        # Предлагаю записать еще 1 игрока.
        more = input("'n' - чтобы завешить запись. ")

    # Закрываю файл.
    golf.close()

def read_golf():
    # Считывает информацию с файла golf.txt.

    # Открываю файл golf.txt в режиме чтения.
    golf = open('golf.txt', 'r')

    # Читаю первую строку в файле.
    name = golf.readline()

    while name != '':
        # Читаю счёт
        points = float(golf.readline())

        # Удаляю \n из имени.
        name = name.rstrip('\n')

        print('Игрок: ', name, '.', sep='')
        print('Заработал(а) -', points, 'балов.')

        # Читаю еще одно имя.
        name = golf.readline()

    # Закрываю файл.
    golf.close()

main()