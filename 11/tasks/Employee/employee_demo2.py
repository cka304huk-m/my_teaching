# Программа демонстрирует класс ShiftSupervisor.

# Имортирую все классы из файла 'employee.py'.
import employee

def main():

    name = input('Имя: ')
    id = int(input('ИД: '))
    salary = float(input('Годовой оклад: '))
    bonus  =float(input('Премия: '))

    # Создаю эезепляр и предаю в него полученные
    # данные выше.
    shiftsuper = employee.ShiftSupervisor(name, id, salary, bonus)

    print()
    print('У нас есть начальник смены который достоен премии:')
    print('Имя:', shiftsuper.get_name(), '\n',
          'ID:', shiftsuper.get_id(), '\n',
          'Годовой оклад:', shiftsuper.get_annual_salary(), '\n',
          'Ему начислен бонус:', shiftsuper.get_production_bonus())

main()