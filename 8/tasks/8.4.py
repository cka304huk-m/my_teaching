# Конвертер азбуки Морзе.

def main():
    """Основная функция."""

    input_text = input('Text: ')

    print('На азбуке Морзе:', converted_text_morze(input_text))

def converted_text_morze(text):
    """Конвертация текста в азбуку Морзе."""

    # Сохраняю аршумент в переменную.
    my_text = text

    # Перекодированое послание.
    text_morze = ''

    # Перебираю текст.
    for t in my_text:
        if t.upper() == ' ':
            text_morze += '  '
        elif t.upper() == ', ':
            text_morze += '-..- '
        elif t.upper() == '. ':
            text_morze += '.-.-.- '
        elif t.upper() == '0':
            text_morze += '----- '
        elif t.upper() == '1':
            text_morze += '.---- '
        elif t.upper() == '2':
            text_morze += '..--- '
        elif t.upper() == '3':
            text_morze += '...-- '
        elif t.upper() == '4':
            text_morze += '....- '
        elif t.upper() == '5':
            text_morze += '..... '
        elif t.upper() == '6':
            text_morze += '-.... '
        elif t.upper() == '7':
            text_morze += '--... '
        elif t.upper() == '8':
            text_morze += '---.. '
        elif t.upper() == '9':
            text_morze += '----. '

    # Возвращаю конвертированный текст.
    return text_morze

# Вызываю основную функцию.
main()
