# Шифрование и дешифрование файлов.

def main():
    """Основная функция."""

    # Азбука морзе.
    morze = codes()

    print(
        """
        Меню:
        0 - Выход
        1 - Зашифровать файл.
        2 - Расшифровать файл.
        """
    )

    choice = ''

    while choice != '0':
        choice = input('Ваш выбор: ')
        if choice == '1':
            try:
                # Назавание незашифровованого файла.
                nfile = input('Название файла, которое прочитаем: ')
                # Прочитанный файл.
                read_f = read_file(nfile)
                # Шифрую файл.
                convert_file(read_f, morze)
                print('Файл converted_morze.txt создан.')
            except FileNotFoundError:
                print('Я не могу найти ваш файл.')
        elif choice == '2':
            try:
                # Закодированный файл.
                con_m = 'converted_morze.txt'
                # Дефифрую файл.
                print(convert_morze(con_m, morze))
            except FileNotFoundError:
                print('Я не могу найти ваш файл.')

def codes():
    """Словарь с русской азбукой Морза."""

    rus_morze = {
        'а': '•-', 'б': '-•••', 'в': '•--', 'г': '--•', 'д': '-••',
        'е': '•', 'ж': '•••-', 'з': '--••', 'и': '••', 'й': '•---',
        'к': '-•-', 'л': '•-••', 'м': '--', 'н': '-•', 'о': '---',
        'п': '•--•', 'р': '•-•', 'с': '•••', 'т': '-', 'у': '••-',
        'ф': '••-•', 'х': '••••', 'ц': '-•-•', 'ч': '---•',
        'ш': '----', 'щ': '--•-', 'ъ': '--•--', 'ы': '-•--',
        'ь': '-••-', 'э': '••-••', 'ю': '••--', 'я': '•-•-',
        '0': '-----', '1': '•----', '2': '••---', '3': '•••--',
        '4': '••••-', '5': '•••••', '6': '-••••', '7': '--•••',
        '8': '---••', '9': '----•',
        '.': '••••••', ',': '•-•-•-',
        ':': '---•••', ';': '-•-•-',
        '(': '-•--•-', ')': '-•--•-',
        "'": '•----•', '"': '•-••-•',
        '—': '-••••-', '/': '-••-•',
        '?': '••--••', '!': '--••--',
        '@': '•--•-•', ' ': ' ',
    }

    return rus_morze

def read_file(filename):
    """Читаю заданый файл"""

    with open(filename, 'r', encoding='utf-8') as read_f:
        data_file = read_f.read()

    read_f.close()

    return data_file

def convert_file(string, morze):
    """Конвертирую данные из строки в азбуку и записываю их
    в новый файл."""

    convert_string = ''

    for s in string:
        # Если в символе есть новая строка, то записать перенос.
        if s == '\n':
            convert_string += '\n'
        elif s == ' ':
            convert_string += ' '
        # Перевести символ в азбуку
        elif s.lower() in morze:
            convert_string += morze[s.lower()] + ' '

    with open('converted_morze.txt', 'w') as con_morze:
        con_morze.write(convert_string)

    con_morze.close()

def convert_morze(con_m, morze):
    """Расшифровываю файл."""

    with open(con_m, 'r') as morze_text:

        text = morze_text.read().split()

    morze_text.close()

    new_text = ''

    for t in text:
        for k, v in morze.items():
            if t == "\n" or t == ' ':
                new_text += t
            elif t == v:
                new_text += k + ' '

    return new_text

main()