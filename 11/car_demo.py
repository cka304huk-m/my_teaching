# Эта программа демоснтрирует класс Car.

import vehicles

def main():
    # Создать объект на основе класса Car.
    # Легковое авто: 2007 Audi c 12500 миль пробега,
    # ценой $21500.00 и с 4 дверьми.
    used_car = vehicles.Car('Audi', 2007, 12500, 21500.0, 4)

    # Показать данные легкового авто.
    print('Изготовитель:', used_car.get_make())
    print('Модель:', used_car.get_model())
    print('Пробег:', used_car.get_mileage())
    print('Цена:', used_car.get_price())
    print('Количество дверей:', used_car.get_doors())

# Вызвать главную функцию.
main()