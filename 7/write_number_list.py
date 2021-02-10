# Эта программа сохраняет список чисел в файл.

def main():
    # Создать список чисел.
    numbers = list(range(1, 8))

    # Открыть файл для записи.
    with open('numberlist.txt', 'w') as outfile:

        # Записать список в файл.
        for item in numbers:
            outfile.write(str(item) + "\n")

    # Закрыть файл.
    outfile.close()

# Вызвать главную функцию.
main()