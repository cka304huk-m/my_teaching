calories_per_day = 500  # потребление калорий в день
weight = float(input('Ваш вес: '))
new_weight = 0
for i in range(1, 7):
    for j in range(1, 31):
        new = weight / calories_per_day
        new_weight += new
    print('За', i, 'месяц, я потеряю', format(new_weight, '.1f'), 'кг.')
