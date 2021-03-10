# Имена и адреса электронной почты.

# Модуль для консервации и расконсервации
# файлов
import pickle

def main():
    """Основная функция"""

    # Словарь со значениями.
    my_dict = read_dict()

    # Меню.
    show_menu(my_dict)

def show_menu(my_dict):
    """Меню приложения."""

    print(
    """
    Меню:
    0 - Выход.
    1 - Отыскать по имени e-mail.
    2 - Добавить имя и e-mail.
    3 - Изменить существующий e-mail.
    4 - Удалить существуещее имя и e-mail.
    """
    )

    # Переменная для выбора пункта в меню.
    choice = ''

    while choice != '0':
        choice = input('Ваш выбор: ')
        if choice == '1':
            find_person(my_dict)
        elif choice == '2':
            add_name_email(my_dict)
        elif choice == '3':
            edit_name(my_dict)
        elif choice == '4':
            del_name(my_dict)

    # Если закрыть програму выбрав меню '0'
    # данные из словаря записываются
    # в файл 'comp.dat'
    compression_dict(my_dict)

def find_person(my_dict):
    """Ишу человека по имени в словаре"""

    name = input('Имя человека: ')
    if name in my_dict:
        print(name, '-', my_dict[name])
    else:
        print('Этого имени нет в словаре.')

def add_name_email(my_dict):
    """Сохраняем данные в словарь"""

    name = input('Имя: ')

    if name not in my_dict:
        email = input('e-mail: ')
        my_dict[name] = email
    else:
        print('Имя уже есть в словаре')

    return my_dict

def edit_name(my_dict):
    """Изменяю e-mail"""

    name = input('Имя: ')

    if name in my_dict:
        email = input('Новая почта: ')
        my_dict[name] = email
    else:
        print("Этого имени нет в словаре.")

def del_name(my_dict):
    """Удаляю пользователя и его e-mail."""

    name = input('Имя: ')

    if name in my_dict:
        print(name, 'успешно удалено из словаря.')
        del my_dict[name]
    else:
        print('Я не могу удалить того кого нет')


def compression_dict(dict_data):
    """Сохраняю словарь в файл."""

    with open('comp.dat', 'wb') as compression:
        pickle.dump(dict_data, compression)

    compression.close()

def read_dict():
    """Расконсервирую файл."""
    try:
        with open('comp.dat', 'rb') as my_dict:
            data = pickle.load(my_dict)

        my_dict.close()

        return data
    # Если файла 'comp.dat' не будет в каталоге,
    # то вернется путой словарь.
    except FileNotFoundError:
        empty_dict = dict()

        return empty_dict

main()