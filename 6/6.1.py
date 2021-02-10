def main():
    filename = 'my_name.txt'

    name = input('Ваше имя: ')

    # Открываю файл чтобы дозаписать в него информацию.
    my_name = open(filename, 'a')

    # Записываю имя в файл.
    my_name.write(name + "\n")

    # Закрываю файл.
    my_name.close()

# Вызываю функцию.
main()