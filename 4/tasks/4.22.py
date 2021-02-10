digit = int(input('Введите неотрицательное целое число: '))

factorial = 1

while digit > 0:
    for i in range(1, digit + 1):
        factorial *= i
        print(i, '-', factorial)
    digit = int(input('Введите неотрицательное целое число: '))