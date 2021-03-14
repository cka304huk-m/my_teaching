import random

# Класс Coin имитирует монету, которую
# можно подбрасывать.

class Coin:

    # Метод __init__ инициализирует
    # атрибуты данных __sideup значением 'Орёл'

    def __init__(self):
        self.__sudeup = 'Орёл'

    # Метод toss генерирует случайное число
    # в диапазоне от 0 до 1. Если это число
    # равно 0, то __sideup получает значение 'Орёл'.
    # В противном случае sideup получает значение 'Решка'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sudeup = 'Орёл'
        else:
            self.__sudeup = 'Решка'

    # Метод get_sideup возвращает значение,
    # на которое ссылается sideup.

    def get_sideup(self):
        return self.__sudeup

# Главная функция.
def main():
    # Создать объект на основе класса Coin.
    my_coin = Coin()

    # Показать обращенную вверх сторону монеты.
    print('Эта сторона обращена вверх:', my_coin.get_sideup())

    # Подбросить монету.
    print('Собираюсь бросить монету десять раз:')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

# Вызвать главную функцию.
main()