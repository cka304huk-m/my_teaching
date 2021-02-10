# Расходы на автомобиль

def main():
    # Основная функция программы.
    print('Введите сколько вы тратите в месяц на:')
    loan_payment = float(input('Платеж по кредиту: '))
    insuarance = float(input('Страховка: '))
    benzin = float(input('Бензин: '))
    oil = float(input('Масло: '))
    tires = float(input('Шины: '))
    maintеnance = float(input('Техобслуживание: '))
    print('За месяц вы тратите на все:',
          format(mount(loan_payment, insuarance, benzin,
                       oil, tires, maintеnance), '.2f'))
    print('А за год это =',
          format(year(loan_payment, insuarance, benzin, oil,
                      tires, maintеnance), '.2f'))

def mount(loan_payment, insuarance, benzin,
                       oil, tires, maintеnance):
    # Расходы за месяц.
    return loan_payment + insuarance + benzin + oil + tires + \
           maintеnance

def year(loan_payment, insuarance, benzin,
                       oil, tires, maintеnance):
    # Расходы за год.
    return 12 * (loan_payment + insuarance + benzin + oil + tires + \
           maintеnance)

# Вызываю главную функцию
main()