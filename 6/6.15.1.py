# Сумма чисел
def main():
    # Переменная для хранения суммы всех чисел.
    total = 0.0

    # Открываю файл numbers.txt в режиме чтения.
    num = open('numbers.txt', 'r')

    for i in num:
        total += float(i)

    print('Общая сумма =', total)

    # Закрываю файл.
    num.close()

# Вызываю главную функцию.
main()