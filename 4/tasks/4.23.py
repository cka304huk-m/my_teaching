start_amount = int(input('Стартовое количество: '))
average_daily_increase = int(input('Среднесуточное увеличение: '))
average_daily_increase /= 100
amount_days = int(input('Кол-во дней для размножения: '))
amount = 0
print('День:\t\t Популяция:')
print('1', "\t\t\t", start_amount)
for i in range(2 ,amount_days + 1):
    new = (start_amount * average_daily_increase)
    start_amount += new
    print(i, "\t\t\t", format(start_amount, '.1f'))