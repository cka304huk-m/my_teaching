# Класс Car.
class Car:

    # Атрибуты.
    def __init__(self, make, year_model, speed=0):
        self.__make = make
        self.__year_model = year_model
        self.__speed = speed

    # Методы модификаторы.
    def accelerate(self, speed=5):
        """При каждом вызове +5
        к скорости."""
        self.__speed += speed

    def break_speed(self, speed=5):
        """При каждом вызове -5
        из скорости."""
        if self.__speed >= 5:
            self.__speed -= speed
        else:
            print('Скорость ниже 5 км.')

    # Методы получатели.
    def get_speed(self):
        """Получить текущию скорость."""
        return self.__speed