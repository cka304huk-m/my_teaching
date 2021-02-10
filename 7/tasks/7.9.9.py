# Данные о населении.

def main():
    """Основная часть программы."""

    # Сохраняю список из функции.
    population = get_file_population()

    # Сохраняю значения которые получаю с функции
    # year_change_population
    min_year, max_year = year_change_population(population)
    print('Среднегодовое изменение численности '
          '\nнаселения за 40 лет =',
          get_change_population(population))

    print('Год с минимальным значением', min_year)
    print('Год с максимальным значением', max_year)

def get_file_population():
    """Считываю данные из файла в пустой список,
    после чего возвращаю список."""

    # Пустой список куда сохраню значения из файла.
    list_populations = []

    # Читаю файл.
    with open('USPopulation.txt', 'r') as population:

        # Перебираю файл в цикле и заношу данные в список,
        # предварительно удалив из данных символ новой строки.
        for popul in population:
            list_populations.append(popul.rstrip("\n"))

    # Закрываю файл.
    population.close()

    # Возвращаю список.
    return list_populations

def get_change_population(population):
    """Получаю данные из списка и считаю среднегодовое
    изменение числености населения в течении указаного периода."""

    # Сохраняю список в переменной.
    list_population = population

    # Переменная для сохранения суммы населения за указанный
    # Промежуток времени.
    total = 0

    # Создаю счётчик годов.
    count_years = 0

    # Перебираю список с населением
    for list in list_population:
        total += int(list)
        count_years += 1

    # Среднее значение
    average_value = total / count_years

    # Возвращаю значение.
    return format(average_value, '.2f')

def year_change_population(population):
    """Год с наибольшим и год с наименьшим изменением населения"""

    # Сохраняю список в переменной.
    list_population = population

    # Нахожу минимальное значение
    min_population = min(list_population)

    # Нахожу максимальное значение
    max_population = max(list_population)

    index_min = 1949 + (list_population.index(min_population) + 1)

    index_max = 1950 + (list_population.index(max_population) + 1)

    return index_min, index_max

main()