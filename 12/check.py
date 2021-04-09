def check(n):
    if (n < 2):
        return (n % 2 == 0)
    return (check(n - 2))

n = int(input('Введите число: '))
if check(n) == True:
    print('Число чётное!')
else:
    print('Число нечетное!')