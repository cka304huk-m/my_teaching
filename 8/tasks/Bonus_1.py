x = int(input())

R = x
a = 0
b = 0
while x != a + b:

    # Остаток от числа
    a += (x % 10) + (x // 10)

    b += x - a

    print('Задано число:', R)
    print(a, b)