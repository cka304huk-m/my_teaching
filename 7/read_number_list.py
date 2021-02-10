# Эта программа считывает числа из файла в список.
numbers = []
def main():
    # Открыть файл для чтения.
    with open('numberlist.txt', 'r') as infile:

        # Прочитать содержимое файла в список.
        for num in infile:
            numbers.append(num)

    # Закрыть файл.
    infile.close()

    # Конвертировать каждый элемент в тип int.
    index = 0
    while index < len(numbers):
        numbers[index] = int(numbers[index])
        index += 1


    # Печатаю содержимое списка
    print(numbers)

# Вызываю главную функцию.
main()