# Программа для записи чисел от 1 до 10
# используя цикл for

def main():

    # Открываю файл для записи чисел.
    my_digits = open('digits.txt', 'w')

    # Перебираю числа от 1 до 10
    # и записываю их в список digits.txt
    for i in range(1, 11):
        my_digits.write(str(i) + "\n")

    # Закрываю файл.
    my_digits.close()

# Вызываю основную функцию.
main()