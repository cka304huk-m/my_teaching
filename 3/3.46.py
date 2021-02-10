year = int(input('Напишите год: '))

if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print('В', year, 'году в феврале 29 дней')
else:
    print('В', year, 'году в феврале 28 дней')