# Гласные и согласные.

def main():
    """Основная функция."""

    # Переменная с гласными буквами.
    vowels = 'ауоыиэяюёе'

    # Получаю текст и сохраняю его в переменной.
    my_string = input('Text: ')
    print('В тексте:')
    print('- гласных:', get_number_vowels(my_string, vowels))
    print('- согласных:', get_number_consonants(my_string, vowels))


def get_number_vowels(string, vowels):
    """Получаю строку и переменную с гласными буквами и считаю количество
    гласных букв в строке."""

    # Счетчик гласных букв.
    count_vowels = 0

    # Перебираю строку и смотрю есть ли буква в строке
    # с гласными буквами.
    for s in string:
        if s.lower() in vowels and s.lower() != ' ':
            count_vowels += 1

    return count_vowels


def get_number_consonants(string, vowels):
    """Получаю строку и переменную с гласными буквами и считаю количество
    согласных букв в строке."""

    # Счетчик согласных букв.
    count_consonants = 0

    # Перебираю строку и смотрю нет ли буквы в строке
    # с гласными буквами.
    for s in string:
        if s.lower() not in vowels and s.lower() != ' ':
            count_consonants += 1

    return count_consonants


# Вызываю основную функцию.
main()