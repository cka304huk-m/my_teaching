import codecs

def main():
    # Создаю переменную-счётчик для подсчета имен девочек.
    count = 0

    # Открываю файл names.txt в режиме чтения.
    names = codecs.open('names.txt', 'r', 'utf-8')

    girl_name = names.readline()
    while girl_name != '':
        girl_name = names.readline().rstrip('\n')
        count += 1

    print('Всего в списке:', count, 'имёни.')

    # Закрываю файл.
    names.close()

# Вызываю главную функцию.
main()