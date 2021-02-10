# Вывод строк используя цикл for

def main():

    # Открываю файл.
    my_strings = open('data.txt', 'r')

    # Использую цикл for чтобы
    # вывести все строчки в файле
    for i in my_strings:
        print(i.strip())


    # Закрываю файл.
    my_strings.close()

# Вызываю гланвую функцию.
main()