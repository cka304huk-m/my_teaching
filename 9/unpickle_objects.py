# Эта программа демонстрирует расконсервацию объектов.
import pickle

# Главная функция.
def main():
    end_of_file = False     # Для обозначения конца файла.

    # Открываю файл для двоичного чтения.
    with open('info.dat', 'rb') as input_file:

        # Прочитать файл до конца.
        while not end_of_file:
            try:
                # Расконсервировать следующий объект.
                person = pickle.load(input_file)

                # Показать объект.
                display_data(person)
            except EOFError:
                # Установить флаг, чтобы обозначить, что
                # был достигнут конец файла.
                end_of_file = True

    # Закрыть файл.
    input_file.close()

# Функция display_data показывает данные о человеке
# в словаре, который передан в качестве аргумента.
def display_data(person):
    print('Имя:', person['имя'])
    print('Возраст:', person['возраст'])
    print('Масса:', person['масса'])
    print()

# Вызываю главную функцию.
main()