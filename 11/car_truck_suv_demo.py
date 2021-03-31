# Эта программа создает объекты Car, Truck
# и SUV.

import vehicles

def main():
    # Создать объект Car для подержанного авто 2001 BMW
    # с 70000 милями пробега, ценой $15000,
    # c 4 дверьми.
    car = vehicles.Car('BMW', 2001, 70000, 15000.0, 4)

    # Создать объект Truck для подержанного пикапа 2002
    # Toyota c 40000 милями пробега, ценой
    # $12000 и с 4-колесным приводом.
    truck = vehicles.Truck('Toyota', 2002, 40000, 12000.0, '4WD')

    # Создать объект SUV для поддержанного 2000
    # Volvo с 30000 милями пробега, ценой
    # $18500 и вместимостью 5 человек.
    suv = vehicles.SUV('Volvo', 2000, 30000, 18500.0, 5)

    print('ПОДЕРЖАННЫЕ АВТО НА СКЛАДЕ',
          "==========================", sep="\n")

    # Показать данные легкового авто.
    print('Данный легковой автомобиль имеется на складе:')
    print('Изготовитель:', car.get_make())
    print('Модель:', car.get_model())
    print('Пробег:', car.get_mileage())
    print('Цена:', car.get_price())
    print('Количество дверей:', car.get_doors())
    print()

    # Показать данные пикапа.
    print('Данный пикап имеется на складе:')
    print('Изготовитель:', truck.get_make())
    print('Модель:', truck.get_model())
    print('Пробег:', truck.get_mileage())
    print('Цена:', truck.get_price())
    print('Тип привода:', truck.get_drive_type())
    print()

    # Показать данные джипа.
    print('Данный джип имеется на складе:')
    print('Изготовитель:', suv.get_make())
    print('Модель:', suv.get_model())
    print('Пробег:', suv.get_mileage())
    print('Цена:', suv.get_price())
    print('Пассажирская вместимость:', suv.get_pass_cap())

# Вызвать главную функцию.
main()