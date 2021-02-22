# Корректор предложений.

def main():
    """Основная функция"""

    # Получаю строковое значение.
    my_string = input('Текст: ')
    print(correct_string(my_string))

def correct_string(string):
    """Корректирую строку."""

    correct = ''

    # Разбиваю строку.
    my_string = string.split()

    my_string[0] = my_string[0].title()

    # Перебираю длину списка минус 1 элемент,
    # так как первое значение мы уже поменяли.
    for i in range(len(my_string) - 1):
        if my_string[i][-1] in '!?.':
            my_string[i + 1] = my_string[i + 1].title()

    for m in my_string:
        correct += m + " "

    return correct

main()