# Самый частотный символ.

def main():
    """Основная функция."""

    my_string = input('Text: ')
    print(frequent_character(my_string))

def frequent_character(string):
    """Самый частый символ в строке"""

    # Сортирую строку от а до я
    # и превращаю в список.
    my_string = sorted(string)

    # Создаю словарь в него буду записывать.
    dublicate = {}

    for s in my_string:
        if s in dublicate:
            dublicate[s] += 1
        else:
            dublicate[s] = 1

    return dublicate

main()