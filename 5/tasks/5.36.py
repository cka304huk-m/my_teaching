# испортирую модуль math
import math

def main():
    # Основная функция
    my_degrees = int(input('Введите градусы: '))
    my = degre45(my_degrees)
    print('Из', my_degrees, 'градусов получаем', my, 'в радианах.')

def degre45(num):
    """Вычисления радианов"""
    my = math.radians(num)
    return my

# Вызываю главную функцию
main()