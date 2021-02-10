def main():
    name_file = input('Имя файла: ')

    # Создать переменную для чтения строк
    count = 0
    # Открываю файл в режиме чтения.
    my_file = open(name_file, 'r')

    # Создаю цикл в котором перебираю файл.
    for my in my_file:
        count += 1
        print(str(count) + ":", my.rstrip('\n'))


    # Закрываю файл.
    my_file.close()

# Вызываю главную функцию.
main()