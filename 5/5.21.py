# Математические тесты.

# импорт генератора случайных чисел.
import random

def main():
    """Основная функция"""
    print('Программа суммирует 2 случайных числа, '
          '\nа после их суммирует.')
    print(summa_digits())

def gen_digits():
    # Генерирует случайные числа.
    a = random.randint(1, 300)
    b = random.randint(1, 300)
    return a, b

def summa_digits():
    # Сумма 2х чисел
    summ = 0
    for i in gen_digits():
        print('+', i)
        summ += i
    return summ

# Вызываю основную функцию.
main()