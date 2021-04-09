# Сумма чисел.

def main():
    # Конечное число.
    n = int(input('Целое число: '))

    print(amount_num(n))

def amount_num(n):
    if n == 1:
        return n
    else:3
        return n + amount_num(n - 1)

main()