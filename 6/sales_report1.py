# Эта программа показывает итоговый объем
# продаж из файла sales_data.txt.

def main():
    # Инициализирировать накопитель.
    total = 0.0

    try:
        # Открыть файл sales_data.txt.
        infile = open('sales_data.txt', 'r')

        # Прочитать значения из файла
        # м накопить их в переменной.
        for line in infile:
            amount = float(line)
            total += amount

        # Закрыть файл.
        infile.close()

        # Распечатать итог.
        print(format(total, '.2f'))

    except FileNotFoundError:
        print('Произошла ошибка при попытке прочитать файл.')

    except ValueError:
        print('В файле найдены нечисловые данные.')

    except:
        print('Произошла ошибка.')

# Вызвать главную функцию.
main()