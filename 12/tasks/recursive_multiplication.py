# Рекурсивное умножение.

def main():
    x1 = int(input('x = '))
    y = int(input('y = '))
    x = 1
    multip(x, x1, y)

def multip(x, x1, y):

    if x <= x1:
        print(y * x)
        return multip(x + 1, x1, y)


main()