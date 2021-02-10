# испорт модуля math
import math

# Создаю главную функцию
def main():
    # Основная функция
    number = int(input('Введите целое число: '))
    root = s_root(number)
    print('Корень из', number, '=', root)


def s_root(num):
    # В ней будем получать квадратный корень
    number = num
    square_root = math.sqrt(number)
    return square_root

# Вызываю главную функцию
main()