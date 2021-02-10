# Игра в угадывание случайного числа.

# Импортирую модуль для генерации чисел.
import random

def main():
    # Основная функция.
    running_programm()

def e_manual():
    # Инструкция.
    print(
        """
        Программа загадывает число от 1 до 100.
        Вы должны угадать загаданное число.
        Для выхода впишите '0'
        """)

def random_digit():
    # Генерирую случайное число от 1 до 100
    d = random.randint(1, 100)
    return d                 # Возвращаю случайное число.


def running_programm():
    # Вся игра тут.
    points = 0
    a = random_digit()
    print(a)
    e_manual()  # Вызываю иструкцию.
    b = int(input('Ваш вариант: '))

    while b != 0:

        if b == a:
            print('\nВаше число и правду =', b)
            print('Вы угадали его потратив всего', points, 'попыток.')
            running_programm()
        elif b > a:
            print('Ваше число', b, 'больше загаданого.')
            points += 1
        elif b < a:
            print('Ваше число', b, 'меньше загаданого.')
            points += 1
        b = int(input('Ваш вариант: '))

main()