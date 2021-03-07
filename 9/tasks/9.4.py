# Уникальные слова.

def main():

    # Название файла который прочитаем.
    nfile = input('Название файла: ')

    # Сохрания список в переменую.
    list_word = read_file(nfile)
    # Вывожу список.
    print(list_word)

def read_file(filename):
    """Читает заданый файл и сохраняет слова из
    него в список."""

    # Читаю переданный файл.
    with open(filename, 'r', encoding='utf-8') as rfile:

        # Сохраняю список в переменной.
        list_word = rfile.read().lower().split()

    # Закрываю файл.
    rfile.close()

    # Возвращаю список уникальных слов.
    return set(list_word)

# Вызываю основную функцию.
main()