speed_transport = int(input('Скорость транспортного средства: '))
amount_hours = int(input('Количество часов которое оно двигалось: '))
print('Час Пройденное расстояние')
print('----------------------------')
for i in range(1, amount_hours + 1):
    print(i, '-', int(speed_transport * i))