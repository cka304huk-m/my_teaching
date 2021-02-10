def main():
    # Инициализирую накапливающию переменную.
    total = 0

    # Открываю файл number_list.txt
    num_list = open('number_list.txt', 'r')

    # Создаю цикл для чтения цифр из входного файла.
    for num in num_list:
        total += int(num)
    print('Общий счёт =', str(total))

    # Закрываю файл.
    num_list.close()

# Вызываю функцию.
main()