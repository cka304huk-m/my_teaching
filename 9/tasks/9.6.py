# Анализ файла.

def main():
    file1 = 'quest.txt'
    file2 = 'quest2.txt'
    rf1 = read_file1(file1)
    rf2 = read_file2(file2)

    uw = unique_words_2_files(rf1, rf2)
    print('Список всех уникальных слов в 2х файлах.')
    print(uw)

    lw = list_words_2_files(rf1, rf2)
    print()
    print('Список слов в 2х файлах.')
    print(lw)

    wl1 = words_1_list(rf1, rf2)
    print()
    print('Список слов из 1 файла, но не входящие в 2 список.')
    print(wl1)

    wl2 = words_2_list(rf1, rf2)
    print()
    print('Список слов из 2 файла, но не входящие в 1 список.')
    print(wl2)

    nibf = not_included_both_files(rf1, rf2)
    print()
    print('Список слов, входящих либо в первый, либо во второй файл, '
          '\nно не входящих в оба файла одновременно.')
    print(nibf)

def read_file1(filename):
    """Читает содержимое файла."""

    with open(filename, 'r', encoding='utf-8') as rfile:
        my = rfile.read().lower().split()

    rfile.close()

    del_symbols = []

    for m in my:
        del_symbols.append(m.strip('.,«»'))

    return del_symbols

def read_file2(filename):
    """Читает содержимое файла."""

    with open(filename, 'r', encoding='utf-8') as rfile:
        my = rfile.read().lower().split()

    rfile.close()

    del_symbols = []

    for m in my:
        del_symbols.append(m.strip('.,«»'))

    return del_symbols

def unique_words_2_files(file1, file2):
    """показывает список всех уникальных слов, 
    содержащихся в обоих файлах."""

    myset = set(file1).union(set(file2))

    return myset

def list_words_2_files(file1, file2):
    """показывает список слов, входящих в оба файла."""

    list1 = file1
    list2 = file2
    list3 = list1 + list2

    return list3

def words_1_list(file1, file2):
    """показывает список слов из первого файла,
    не входящих во второй."""

    list1 = set(file1)
    list2 = set(file2)
    total = list1.difference(list2)

    return total

def words_2_list(file1, file2):
    """показывает список слов из первого файла,
    не входящих во второй."""

    list1 = set(file1)
    list2 = set(file2)
    total = list2.difference(list1)

    return total

def not_included_both_files(file1, file2):
    """показывает список слов, входящих либо в первый,
    либо во второй файл, но не входящих в оба файла
    одновременно."""

    list1 = set(file1)
    list2 = set(file2)
    total = list1.symmetric_difference(list2)

    return total

main()