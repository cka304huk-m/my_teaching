import car

def main():
    make = input('Производитель машины: ')
    year_model = int(input('Год выпуска: '))
    speed = int(input('Скорость в км/ч: '))

    # Создаю экзепляр.
    my_car = car.Car(make, year_model, speed)

    print('Текущая скорость -',my_car.get_speed(), 'км/ч.')

    # 5 раз вызываю accelerate() - это + 25 км
    print()
    print("Сейчас 5 раз я увеличу скорость.")
    my_car.accelerate()
    print('Текущая скорость -', my_car.get_speed(), 'км/ч.')
    my_car.accelerate()
    print('Текущая скорость -', my_car.get_speed(), 'км/ч.')
    my_car.accelerate()
    print('Текущая скорость -', my_car.get_speed(), 'км/ч.')
    my_car.accelerate()
    print('Текущая скорость -', my_car.get_speed(), 'км/ч.')
    my_car.accelerate()
    print('Текущая скорость -', my_car.get_speed(), 'км/ч.')

    # 5 раз вызываю break_speed() - это - 25 км
    print()
    print("Сейчас 5 раз я буду уменьшать скорость.")
    my_car.break_speed()
    print('Текущая скорость -', my_car.get_speed(), 'км/ч.')
    my_car.break_speed()
    print('Текущая скорость -', my_car.get_speed(), 'км/ч.')
    my_car.break_speed()
    print('Текущая скорость -', my_car.get_speed(), 'км/ч.')
    my_car.break_speed()
    print('Текущая скорость -', my_car.get_speed(), 'км/ч.')
    my_car.break_speed()
    print('Текущая скорость -', my_car.get_speed(), 'км/ч.')

main()