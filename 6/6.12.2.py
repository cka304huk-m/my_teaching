def main():
    # Запрашиваю название файла.
    name_file = input('Название файла: ')

    # Открываю запрошенный файл
    my_file = open(name_file, 'r')

    # Создаю счетчик строк.
    count_strings = 0

    while count_strings != 5:
        print(my_file.readline().rstrip('\n'))
        count_strings += 1

    # Закрыть файл.
    my_file.close()

# Вызвать главную функцию.
main()