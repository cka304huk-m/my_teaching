def main():
    # Открываю файл numbers.txt в режиме чтения.
    num = open('numbers.txt', 'r')

    # Читаю содержимое файла и печаю его на экран.
    print(num.read())

    # Закрываю файл.
    num.close()

# Вызываю главную функцию.
main()