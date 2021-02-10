# Эта программа преобразует скорости от 60
# до 130 км/ч (с приращениеми в 10 км)
# в mph.

START_SPEED = 60            # Начальная скорость.
END_SPEED = 131             # Конечная скорость.
INCREMENT = 10              # Приращение скорости.
CONVERSION_FACTOR = 0.6214  # Коэффицент пересчёта.

# Напечатать заголовки таблицы.
print('КPH - MPH')
print('--------------')

# Напечатать скорости.
for kph in range(START_SPEED, END_SPEED, INCREMENT):
    mph = kph * CONVERSION_FACTOR
    print(kph, ' - ', format(mph, '.1f'))