# Эта программа показывает записи
# из файла coffee.txt.

def main():
    # Открыть файл coffee.txt.
    coffee_file = open('coffee.txt', 'r')

    # Прочитать поле с описание первой записи.
    descr = coffee_file.readline()

    # Прочитать остаток файла.
    while descr != '':
        # Прочитать поле с количеством.
        qty = float(coffee_file.readline())

        # Удалить \n из описания.
        descr = descr.rstrip('\n')

        # Показать запись.
        print('Описание:', descr)
        print('Количество:', qty, '\n')

        # Прочитать следующее описание.
        descr = coffee_file.readline()

    # Закрыть файл.
    coffee_file.close()

# Вызвать главную функцию.
main()