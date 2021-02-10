def main():
    # Переменная для суммирования всех чисел из прочитаного
    # файл numbers.txt.
    total = 0

    # Переменная для подмсчета количества чисел.
    amount = 0
    try:
        # Открываю файл numbers.txt в режиме чтения.
        numbers = open('numbers.txt', 'r')

        # Использую цикл for для сумирования прочитаных чисел
        # и подсчёта строк.
        for num in numbers:
            amount += 1
            total += float(num)
        arithmetical_mean = total // amount
        print('Среднее арефметическое =', arithmetical_mean)

        # Закрываю файл.
        numbers.close()
    except FileNotFoundError as IO:
        print(IO)
    except ValueError as VE:
        print(VE)
    except UnboundLocalError as UE:
        print(UE)

# Вызываю главную функцию.
main()