# Генерация простого числа.

def main():
    """Функция для передачи всех параметров."""
    numbers = input_number()
    g_list = gen_list(numbers)
    prime_сomposite_numbers(numbers, g_list)

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

def prime_сomposite_numbers(n, list_num):
    """Проверка списка на простые и составные числа"""
    composite_numbers = []
    prime_numbers = []
    l_num = list_num

    while len(l_num) != 0:
        print(l_num)
        for numb in l_num:
            if numb == 2:
                prime_numbers.append(numb)
                l_num.remove(numb)
            elif numb % 2 == 0:
                composite_numbers.append(numb)
                l_num.remove(numb)
            elif numb % 3 == 0:
                composite_numbers.append(numb)
                l_num.remove(numb)
            else:
                prime_numbers.append(numb)
                l_num.remove(numb)

    print('Простые числа:')
    print(sorted(prime_numbers))
    print('Составные числа:')
    print(sorted(composite_numbers))

main()


