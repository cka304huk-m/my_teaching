def main():
    # Открываю файл number_list.txt в режиме дозаписи.
    num_list = open('number_list.txt', 'r')

    num = num_list.read()
    print(num)

    # Закрываю файл.
    num_list.close()

# Вызываю функцию.
main()