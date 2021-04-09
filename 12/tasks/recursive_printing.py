# Рекурсивная печать.

def main():
    # Печатать от:
    i = 1
    # Печатать до:
    n = int(input('Целое число: '))

    printing(i, n)

def printing(i, n):

    if i <= n:
        print(i)
        return printing(i + 1, n)

main()