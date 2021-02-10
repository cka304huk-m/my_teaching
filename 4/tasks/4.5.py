# Средняя толщина дождевых осадков за несколько лет.

amount_age = int(input('За сколько лет: '))
mount = 0
amount_rain = 0

for i in range(amount_age):
    for j in range(1, 13):
        mm_rain = float(input('Сколько мм дождя: '))
        print(j, '=', mm_rain, 'милиметров дождя.')
        mount += 1
        mm = mm_rain * j
        amount_rain += mm
average = amount_rain / 12
print('Я наблюдал за', mount, 'месяцами.')
print('Общая толщина осадков соствила:', amount_rain, 'мм.')
print('Средняя толщина осадков в месяц:', average)