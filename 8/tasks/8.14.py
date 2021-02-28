# Цены на бензин.

def main():
    """Основная функция"""

    print('Цены на бензин.\n')
    print(
        """
        Меню:
        0 - Выход.
        1 - Средняя цена бензина за каждый год из списка.
        2 - Средняя цена бензина за месяц в году из списка.
        3 - Наибольшая и наименьшая цена в году из списка.
        4 - Сгенерировать текстовый файл 'ascendingGasPrice.txt' с ценовой по возрастанию.
        5 - Сгенерировать текстовый файл 'descendingGasPrice.txt' с ценой по убыванию.
        """
    )
    choice = int(input('Ваш выбор: '))
    # Полученый список из функции,
    # сохраняю в переменую.
    years_mounts = read_file()
    while choice != 0:
        if choice == 1:
            # Полученые списки из функции,
            # сохраняю в переменые.
            ya, pa = annual_average(years_mounts)

            print('Средняя цена бензина за год:')
            for i in range(len(ya)):
                print(ya[i], pa[i], sep=" - ", end='. ')
            print()

        elif choice == 2:
            # Полученые списки из функции,
            # сохраняю в переменые.
            ym, pm = average_monthly_price(years_mounts)
            print('Средняя цена бензина за месяц в году:')
            for i in range(len(ym)):
                print(ym[i], pm[i], sep=" - ", end='. ')
            print()

        elif choice == 3:
            # Полученые строки из функции,
            # сохраняю в переменые.
            min_p, max_p = highest_lowest_prices_year(years_mounts)
            print('Наибольшая и наименьшая цена в году:')
            print('Минимальная: ', min_p, end='. ')
            print('Максимальная: ', max_p, '.', sep='')

        elif choice == 4:
            # Генерация цен в файл 'ascendingGasPrice.txt'
            # на бензин по возрастанию.
            date_price_ascending(years_mounts)

        elif choice == 5:
            # Генерация цен в файл 'descendingGasPrice.txt'
            # на бензин по убыванию.
            date_price_descending(years_mounts)

        choice = int(input('Ваш выбор: '))


def read_file():
    """Считываю данные из файла."""

    # Название файла.
    filename = 'GasPrices.txt'

    # Списки для сохранения значений.
    years_mounts = []
    years = []

    # Читаю файл.
    with open(filename, 'r', encoding='utf-8') as gasPrice:

        # Перебираю данные из файла.
        for gp in gasPrice:

            # Сохраняю месяц и год
            years_mounts.append(gp[:].rstrip('\n'))


    # Закрываю файл.
    gasPrice.close()

    # Возвращаю полученые данные.
    return years_mounts

def annual_average(years_mounts):
    """Средняя цена за год."""

    # Списки с годами и ценами.
    list_years = list()
    list_prices = list()

    # Переменная содержащая первый год из
    # списка для проверки.
    start_year = int(years_mounts[0][6:10])

    # Переменная для складывания значений.
    total = 0
    # Переменная для подсчета значений при
    # определеном условии.
    count = 0

    # Перебираю список.
    for y in range(len(years_mounts)):
        # Если год в списке = году из проверочной
        # переменной.
        if int(years_mounts[y][6:10]) == start_year:
            # Записываю значения из списка в переменную
            # и перевожу его в float, так как число с точкой.
            total += float(years_mounts[y][11:])
            # Считаю кол-во значений в текущем году.
            count += 1

        # Если стартового года нет в списке.
        if start_year not in list_years:
            # Записываю год в список.
            list_years.append(start_year)
            # Ищу среднее значение за год.
            div_tc = format(total / count, '.2f')
            # Записываю среднее значение за год в
            # список.
            list_prices.append(float(div_tc))

        # Если год из списка != году из проверочной
        # переменной.
        elif int(years_mounts[y][6:10]) != start_year:
            # Прибавляю к году + 1
            start_year += 1

    # Возвращаю списки с годами и ценами.
    return list_years, list_prices

def average_monthly_price(years_mounts):
    """Средняя цена за месяц"""

    # Списки с годами/месяцами и ценами.
    list_years_mounts = list()
    list_prices = list()

    # Переменная содержащая первый месяц и
    # год из списка для проверки.
    start_mount = int(years_mounts[0][0:2])
    start_year = int(years_mounts[0][6:10])

    # Переменная для складывания значений.
    total = 0
    # Переменная для подсчета значений при
    # определеном условии.
    count = 0

    # Перебираю список.
    for y in range(len(years_mounts)):
        # Если год и месяц в списке = году и месяцу
        # из проверочной переменной.
        if int(years_mounts[y][6:10]) == start_year \
                and int(years_mounts[y][:2]) == start_mount:
            # Записываю значения из списка в переменную
            # и перевожу его в float, так как число с точкой.
            total += float(years_mounts[y][11:])
            # Считаю кол-во значений в текущем году.
            count += 1

        # Если стартового месяца и года нет в списке.
        str_mount_year = str(start_mount) + "-" + str(start_year)
        if str_mount_year not in list_years_mounts:
            # Записываю месяц и год в список.
            list_years_mounts.append(str_mount_year)
            # Ищу среднее значение за год.
            div_tc = format(total / count, '.2f')
            # Записываю среднее значение за год в
            # список.
            list_prices.append(float(div_tc))

        # Если месяц из списка != стартовому месяцу и
        # год из списка = стартовому году.
        elif int(years_mounts[y][:2]) != start_mount \
                and int(years_mounts[y][6:10]) == start_year:
            # Если в стартовый месяц < 12.
            if start_mount < 12:
                # Добавляю к стартовому месяцу + 1
                start_mount += 1
            # Иначе.
            else:
                # Добавляю к стартовому году + 1
                start_year += 1

        # Если месяц из списка != месяцу из переменой стартового
        # месяца и год из списка != году из перменной стартового
        # года.
        elif int(years_mounts[y][:2]) != start_mount \
                and int(years_mounts[y][6:10]) != start_year:
            # Переменной стартового месяца присваиваю 1.
            start_mount = 1
            # К переменной стартового месяца добавляю +1.
            start_year += 1

    # Возвращаю списки.
    return list_years_mounts, list_prices

def highest_lowest_prices_year(years_mounts):
    """Наибольшая и наименьшая цены в году:
    в течение каждого года в файле определяет
    дату и величину самой низкой и самой высокой цены."""

    # Список цен.
    prices = []

    # Перебираю список.
    for i in range(len(years_mounts)):
        # Приравниваю их к float() и записываю в список.
        prices.append(float(years_mounts[i][11:]))

    # Строки для сохранения даты
    # минимального и максимального значения.
    min_prices = ''
    max_price = ''

    # Перебираю список.
    for i in range(len(years_mounts)):
        # Если минимальная цена = значению из списка.
        if float(years_mounts[i][11:]) == min(prices):
            # Записываю в переменую.
            min_prices = years_mounts[i]
        # Или значения из списка = максимальному значению
        # из списка.
        elif float(years_mounts[i][11:]) == max(prices):
            # Записываю в переменую.
            max_price = years_mounts[i]

    # Возвращаю минимальное и максимальное значение.
    return min_prices, max_price

def date_price_ascending(years_mounts):
    """Список цен, упорядоченный по возрастанию: генерирует 
    текстовый файл, в котором даты и цены отсортированы в 
    возрастающем порядке."""

    ym = years_mounts[:]

    # Список с ценами.
    prices = []

    # Перебираю список и записываю цены в список.
    for i in range(len(ym)):
        if float(ym[i][11:]):
            prices.append(float(ym[i][11:]))

    # Список где цены с годами будут идти по возрастанию.
    ascending_price = []

    # Переменная для поиска индекса.
    index_p = 0

    # Выполняю цикл пока длина списка != 0
    while len(prices) != 0:
        # Если минимальная цена есть в списке.
        if min(prices) in prices:
            # Узнаю его индекс и сохраняю в переменой.
            index_p = prices.index(min(prices))
            # Удаляю значение из списка по полученому индексу.
            del prices[index_p]
            # Записываю значение в новый список.
            ascending_price.append(ym[index_p])
            # Удаляю значения из списка по полученому индексу.
            del ym[index_p]

    # Создаю новый файл, в который записываю полученую информацию.
    with open('ascendingGasPrice.txt', 'w') as asGP:

        # Перебираю список
        for ap in ascending_price:
            # Записываю значения в файл.
            asGP.write(str(ap) + "\n")

    # Закрываю файл.
    asGP.close()

def date_price_descending(years_mounts):
    """Список цен, упорядоченный по возрастанию: генерирует
        текстовый файл, в котором даты и цены отсортированы в 
        возрастающем порядке."""
    ym = years_mounts[:]

    # Список с ценами.
    prices = []

    # Перебираю список и записываю цены в список.
    for i in range(len(ym)):
        if float(ym[i][11:]):
            prices.append(float(ym[i][11:]))

    # Список где цены с годами будут идти по убыванию.
    descending_price = []

    # Переменная для поиска индекса.
    index_p = 0

    # Выполняю цикл пока длина списка != 0
    while len(prices) != 0:
        # Если минимальная цена есть в списке.
        if max(prices) in prices:
            # Узнаю его индекс и сохраняю в переменой.
            index_p = prices.index(max(prices))
            # Удаляю значение из списка по полученому индексу.
            del prices[index_p]
            # Записываю значение в новый список.
            descending_price.append(ym[index_p])
            # Удаляю значения из списка по полученому индексу.
            del ym[index_p]

    # Создаю новый файл, в который записываю полученую информацию.
    with open('descendingGasPrice.txt', 'w') as dGP:

        # Перебираю список
        for de in descending_price:
            # Записываю значения в файл.
            dGP.write(str(de) + "\n")

    # Закрываю файл.
    dGP.close()

main()