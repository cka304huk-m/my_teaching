# Оценщик малярных работ
import math

# Глобальные константы
SQUARE_METER = 2                # На 1 кв. м. нужно 2 литра краски.
WORK_HOUR_SQUARE_METER = 0.8    # За 1 час я покрашу 0.8 кв. м.
PRICE_WORK_HOUR = 2000

def main():
    # Основная функция.
    square = float(input('Площадь покраски: '))
    paint = float(input('Цена 5 л. краски: '))
    print('Количество требующихся емкостей краски:',
          int(number_of_paint_containers(square)))
    print('Количество требующихся рабочих часов:',
          int(working_hours(square)))
    print('Стоимость краски:', price_paint(square, paint))
    print('Стоимость работы:', price_work(square))
    print('Общая стоимость малярных работ:', all_price(square, paint))

def number_of_paint_containers(square):
    if square % 5 == 0:
        return square / 5
    else:
        return math.ceil(square / 5)

def working_hours(square):
    return square / WORK_HOUR_SQUARE_METER

def price_paint(square, paint):
    return number_of_paint_containers(square) * paint

def price_work(square):
    return working_hours(square) * PRICE_WORK_HOUR

def all_price(square, paint):
    return price_paint(square, paint) + price_work(square)

main()