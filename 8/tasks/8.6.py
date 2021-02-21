# Среднее количество слов.

# Название файла с текстом.
filename = 'text.txt'

def read_file(file):
    """Читаю файл"""

    # Пустая строка для сохрания данных из файла.
    my_text = ''

    # Читаю файл.
    with open(file, 'r', encoding='utf-8') as rfile:

        # Перебираю данные из файла.
        for r in rfile.read():
            # Сохраняю все в пустую строку.
            my_text += r

    # Закрываю файл.
    rfile.close()

    # Возвращаю полученную строку.
    return my_text

def average_word_count(my_string):
    """Среднее количество слов на предложение."""

    # Всего предложений.
    count_dot = 0

    for dot in my_string:
        if dot == '.':
            count_dot += 1
    print('В тексте -', count_dot, 'предложения.')

    # Меняю запятые на пробелы, для формирования списка слов
    # и их подсчета в будущем.
    replace_text = my_string.replace(',', '')

    words = len(replace_text.split())
    print('Всего слов -', words)

    average = int(words) / int(count_dot)
    print('Среднее количество слов на предложение -', int(average))

print(read_file(filename))
average_word_count(read_file(filename))