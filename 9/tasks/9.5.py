# Частотность слов.

def main():
    """Основная функция."""

    namefile = input('Файл который читаем: ')
    # Сохраняю список из прочитаного файла.
    rfile = read_file(namefile)
    # Удаляю символы ., из списка и сохраняю в новый
    # список
    del_symb = del_symbols(rfile)

    print('Слово в тексте и кол-во его повторений в тексте:')
    for k, v in count_word(del_symb).items():
        print(k, '=', v)

def read_file(filename):
    """Считываю содержимое файла в строку."""

    with open(filename, 'r', encoding='utf-8') as rfile:
        # Сохраняю в список и делаю символы с маленькой буквы.
        my_string = rfile.read().lower().split()

    rfile.close()

    return my_string

def del_symbols(my_list):
    """Удаление знаков припенания в списке."""

    # Список для сохрания слов после удаления знаков препинания.
    del_symbol_list = []

    # Перебираю список.
    for l in my_list:
        # Удаляю из слова знаки препинания.
        del_symbol_list.append(l.strip('.,«»'))

    return del_symbol_list

def count_word(my_list):
    """Считаю сколько раз в слове встречается заданое слово
    и сохраняю его в словаре, как слово ключ, а значение
    кол-во раз повторения слова в списке."""

    # Пустой словарь в него буду сохранять слово и его повторения.
    c_word = {}

    # Перебираю список.
    for my in my_list:
        # Если слова нет в словаре.
        if my not in c_word:
            # Сохраняю слово и его кол-во повторений.
            c_word[my] = my_list.count(my)

    return c_word

# Вызываю основную функцию.
main()