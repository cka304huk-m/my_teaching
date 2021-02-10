amount_days = int(input('Количество дней: '))
days = amount_days
all_amount = 0
amount = 0
print('День    Сумма')
while days > 0:
    for i in range(1, days + 1):
        if i == 1:
            days -= 1
            amount = 1
            all_amount += amount
            print(i, '   ', amount)
        else:
            days -= 1
            amount *= 2
            all_amount += amount
            print(i, '   ', amount)
rub = all_amount // 100
kop = all_amount % 100
print('Всего за', amount_days, 'ты заработал:',rub, 'рублей и', kop, 'копеек.')