# Вывод строк используя цикл while

def main():

    # Открываю файл.
    my_strings = open('data.txt', 'r')

    # Читаю одну строку, она мне понадобиться
    # для выполнения цикла
    line = my_strings.readline()

    # Выподняю цикл пока не будет пустой строки.
    while line != '':
        print(line.rstrip())
        line = my_strings.readline()

    # Закрываю файл.
    my_strings.close()

# Вызываю гланвую функцию.
main()