# Словарный индекс.

def main():
    """Основная функция."""

    # Название файла, которое читаем.
    filename = 'Kennedy.txt'
    lines, words = read_file(filename)
    dict_w = word_dict(lines, words)
    write_file(dict_w)



def read_file(filename):
    """Читаю переданный файл"""

    with open(filename, 'r', encoding='utf-8') as kenedy:
        # Читаю одну строку в файле.
        text_kenedy = kenedy.read()

    kenedy.close()
    lines = text_kenedy.split('\n')
    words = text_kenedy.split()

    return lines, words

def word_dict(lines, words):

    # Пустой словарь куда сохраняю ключ(слово),
    # а значение(номер строки)
    wd = dict()

    for w in words:
        if w not in wd:
            wd[w] = []
            for l in range(len(lines)):
                if w in lines[l]:
                    wd[w].append(l + 1)


    return wd

def write_file(dict_w):
    """Записываю данные из словаря в файл."""

    with open('Index.txt', 'w') as index:

        for k, vl in dict_w.items():
                input_text = k + ': ' + str(vl).strip('[]')
                index.write(input_text + "\n")

    index.close()

main()