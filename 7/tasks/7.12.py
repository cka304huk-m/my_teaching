# Генерация простого числа.

def main():
    """Функция для передачи всех параметров."""
    numbers = input_number()
    g_list = gen_list(numbers)
    prime, composite = prime_сomposite_numbers(g_list)
    print('Простые числа: ', end='')
    print(prime)
    print('Составные числа: ', end ='')
    print(composite)

def input_number():
    """Просит пользователя ввести число больше 1"""
    try:
        num = int(input('Число которое больше 1: '))

        if num < 2:
            num = 2
            print('Вы хотели меня обхитрить поэтому я ввел число за вас.'
                  '\nТеперь оно равно = 2.')

        return num

    except ValueError:
        print('Разрешено вводить только целое число!')


def gen_list(num):
    """Получаю число из функции и на оснавании его генерирую список
    c 2 до полученого числа."""
    gen_list_ = list(range(2, num + 1))

    return gen_list_

def prime_сomposite_numbers(list_num):
    """Проверка списка на простые и составные числа"""

    # Список составных чисел.
    composite_numbers = []

    # Список простых чисел.
    prime_numbers = []

    # Переменная для подсчёта множителей.
    count = 0

    # Перебираю числа в списке.
    for num in list_num:
        # Перебираю числа от 2 до текущего числа.
        for n in range(2, num):
            if num % n == 0:
                count += 1

        if count == 0:
            prime_numbers.append(num)
        else:
            count = 0
            composite_numbers.append(num)

    # Вовзаращаю списки с числами.
    return prime_numbers, composite_numbers

main()


