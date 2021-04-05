# Сотрудник.

# Импортирую классы: Employee и ProductionWorker
import employee

def main():

    name = input('Имя сотрудника: ')
    id = input('ИД: ')
    number_shift = int(input('Номер смены, 1 - день, 2 - ночь: '))
    rate = float(input('Почасовая ставка: '))

    # Создаю экземпляр ProductionWorker
    pw = employee.ProductionWorker(name, id, number_shift, rate)

    print()
    print('Вот что я знаю:')
    # Вызываю методы получатели и вывожу всю информацию о рабочем.
    print('Имя:', pw.get_name())
    print('ИД:', pw.get_id())
    print('Сотрудник работает в', pw.get_shift_num())
    print('Почасовая ставка =', pw.get_rate_hourly())

main()