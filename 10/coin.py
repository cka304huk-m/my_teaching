import random

# Класс Coin имитирует монету, которую
# можно подбрасывать (теперь это модуль, который храниться в файле.

class Coin:

    # Метод __init__ инициализирует
    # атрибут данных __sideup значением 'Орёл'

    def __init__(self):
        self.__sideup = 'Орёл'

    # Метод toss генерирует случайное число
    # в диапазоне от 0 до 1. Если это число
    # равно 0, то __sideup получает значение 'Орёл'.
    # В противном случае sideup получает значение 'Решка'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Орёл'
        else:
            self.__sideup = 'Решка'

    # Метод get_sideup возвращает значение,
    # на которое ссылается sideup.

    def get_sideup(self):
        return self.__sideup