# Рекурсивный метод возведения в степень.

def main():
    num = int(input('Число: '))
    exp = int(input('Возвести в спень: '))

    print(exponentiation(num, exp))

def exponentiation(num, exp):
    if exp == 1:
        return num
    else:
        return num * exponentiation(num, exp - 1)

main()