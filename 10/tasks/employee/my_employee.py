import pickle
from employee import Employee

def main():
    # Данные которые доступны после закрытия программы.
    filename = 'save_employees.dat'

    # Читает сохраненый файл, если его нет, возращает пустой
    # Словарь.
    dict_employees = empty_dict(filename)

    menu(dict_employees, filename)

def menu(dict_employees, filename):
    """Меню."""
    print(
        'Меню:',
        '1 - Найти сотрудника по id.',
        '2 - Добавить нового сотрудника по id.',
        '3 - Изменить имя, отдел и должность существующего сотрудника.',
        '4 - Удалить сотрудника по id.',
        '5 - Выйти.', sep='\n'
    )

    choice = 0

    while choice != 5:
        choice = int(input('\nВаш выбор: '))
        if choice == 1:
            find_employee(dict_employees)
        elif choice == 2:
            add_employee(dict_employees, filename)
        elif choice == 3:
            edit_employee(dict_employees, filename)
        elif choice == 4:
            del_employee(dict_employees, filename)

    save_employees(dict_employees, filename)

def empty_dict(filename):
    """Возвращаю данные из словаря"""
    try:
        with open(filename, 'rb') as input_file:
            my_data = pickle.load(input_file)
            return my_data
    except FileNotFoundError:
        empty = dict()

        return empty

def find_employee(dict_employees):
    """Найти сотрудника в словаре."""

    id = input('Идентификационный номер: ')

    if id in dict_employees:
        n, d, f = dict_employees[id]
        print('\nИнформация по сотруднику:')
        print('Имя:', n)
        print('ИД:', id)
        print('Отдел:', d)
        print('Должность:', f)
    else:
        print('Нет такого сотрудника.\n')

def add_employee(dict_employees, filename):
    """Добавить сотрудника в словарь"""

    id = input('Идентификационный номер: ')

    if id not in dict_employees:
        name = input('Имя: ')
        id = input('ИД: ')
        division = input('Отдел: ')
        function = input('Должность: ')
        new_employee = Employee(name, id, division, function)
        dict_employees[id] = []
        dict_employees[id].append(new_employee.get_name())
        dict_employees[id].append(new_employee.get_division())
        dict_employees[id].append(new_employee.get_function())
        save_employees(dict_employees, filename)
    else:
        print('Уже есть сотрудник под этим номером, выберите другой.\n')

def edit_employee(dict_employees, filename):
    """Изменение информации о сотруднике."""

    id = input('Идентификационный номер: ')

    if id in dict_employees:
        print('Введите новые данные:')
        name = input('Имя: ')
        division = input('Отдел: ')
        function = input('Должность: ')
        edit_empl = Employee(name, id, division, function)
        dict_employees[id][0] = edit_empl.get_name()
        dict_employees[id][1] = edit_empl.get_division()
        dict_employees[id][2] = edit_empl.get_function()
        print('Информация о сотруднике обновлена.\n')
        save_employees(dict_employees, filename)
    else:
        print('Нет такого сотрудника.\n')

def del_employee(dict_employees, filename):
    """Удалить сотрудника из базы."""
    id = input('Идентификационный номер: ')

    if id in dict_employees:
        del dict_employees[id]
        print('Сотрудник id №', id, '. Успешно удален.\n', sep='')
        save_employees(dict_employees, filename)
    else:
        print('Нет такого сотрудника.\n')

def save_employees(dict_employees, filename):
    """Законсервировать файл."""

    with open(filename, 'wb') as outfile:
        pickle.dump(dict_employees, outfile)

main()