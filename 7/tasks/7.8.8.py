# Поиск имени

def main():
    # Основная функция.

    # Пустой список куда буду складывать 2 имени,
    # а потом проходить циклом и сравнивать есть
    # ли они в списке популрных имен.
    boy_girl = []

    print(
        """
        Меню:
        1 - Популярность женского имени
        2 - Популярность мужского имени.
        3 - Популярность мужского и женского имени.
        """)
    choice = int(input('Сделайте выбор: '))

    if choice == 1:
        name = input('Напишите имя: ')
        if name.title() in get_girls_name():
            print('Имя находиться среди популярных имен.')
        else:
            print('Имя не популярно.')
    elif choice == 2:
        name = input('Напишите имя: ')
        if name.title() in get_boys_name():
            print('Имя находиться среди популярных имен.')
        else:
            print('Имя не популярно.')
    elif choice == 3:
        # Добавляю имена в список для
        # будущего их сравнения со списками.
        while len(boy_girl) != 2:
            name = input('Имя: ')
            boy_girl.append(name)

        for bg in boy_girl:
            if bg in get_girls_name() or bg in get_boys_name():
                print(bg, '- популярное имя.')
            else:
                print(bg, '- не популярно.')


def get_girls_name():
    # Считываю в список имена девочек из файла.

    # Пустой список куда буду записывать имена девочек.
    name_girls = []

    # Читаю файл.
    with open('GirlNames.txt', 'r') as girls:

        # Прохожу имена в цикле и записываю их в список
        # предварительно удалив символ новой строки.
        for girl in girls:
            name_girls.append(girl.rstrip('\n'))

    # Закрываю файл.
    girls.close()

    # Возвращаю список с именами девочек.
    return name_girls

def get_boys_name():
    # Считываю в список имена мальчиков из файла.

    # Пустой список куда буду записывать имена мальчиков.
    name_boys = []

    # Читаю файл.
    with open('BoyNames.txt', 'r') as boys:

        # Прохожу имена в цикле и записываю их в список
        # предварительно удалив символ новой строки.
        for boy in boys:
            name_boys.append(boy.rstrip("\n"))

    # Закрываю файл.

    # Возвращаю список с именами мальчиков.
    return name_boys

# Вызываю основную функцию
main()