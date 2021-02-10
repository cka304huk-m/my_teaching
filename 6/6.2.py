def main():
    # Открываю файл my_name.txt.
    my_name = open('my_name.txt', 'r')

    # Читаю файл.
    for name in my_name:
        famaly = name.rstrip("\n")
        print(famaly)

    # Закрываю файл.
    my_name.close()

# Вызываю функцию.
main()