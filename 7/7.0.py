# Статистика дождевых осадков.

# В 1 годе 12 месяцев
YEAR = 12

# Список с данными за 12 месяцев(1 год).
rain_list = [0] * YEAR

def main():
    # Основная функция.

    # Заполняю список с данными за каждый месяц.
    for y in range(YEAR):
        print('Осадки за', y + 1, 'месяц:')
        rain_list[y] = float(input())

    print('Суммарное кол-во осадков за 1 год:', rain_sum(rain_list))
    print('Среднее кол-во осадков:', rain_mean(rain_list))
    rain_min_max(rain_list)


def rain_sum(list_rain):
    # Сумарное кол-во дождевых осадков за 1 год.
    total = 0
    for rain in list_rain:
        total += rain

    return total


def rain_mean(list_rain):
    # Среднее ежемесячное кол-во осадков.
    total = rain_sum(list_rain) / YEAR
    return total

def rain_min_max(list_rain):
    # Месяцы с самым высоким и
    # самым низким количеством дождевых осадков.
    min_rain = min(list_rain)
    max_rain = max(list_rain)

    print('Минимальное', min_rain, 'в', list_rain.index(min_rain) + 1)
    print('Максимальное', max_rain, 'в', list_rain.index(max_rain) + 1)

main()
