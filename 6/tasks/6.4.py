def main():
    # Открываю файл number_list.txt
    num_list = open('number_list.txt', 'r')

    # Создаю цикл для чтения цифр из входного файла.
    for num in num_list:
        number = num.rstrip("\n")
        print(number)

    # Закрываю файл.
    num_list.close()

# Вызываю функцию.
main()