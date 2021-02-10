digit = 0
amount = 0

while digit >= 0:
    digit = int(input('Введите положительное число: '))
    if digit > 0:
        amount += digit
    else:
        print('Число отрицальное или равно 0!')
print('Прошайте! Сумма положительных чисел =', amount)