def main():
    # Открываю входной файл number_list.txt в режиме записи.
    num_list = open('number_list.txt', 'w')

    # Применяю цикл для генерации чисел от 1 до 100
    # и записи их в файл number_list.txt.
    for i in range(1, 101):
        num_list.write(str(i) + "\n")

    # Закрываю файл.
    num_list.close()

# Вызываю функцию.
main()