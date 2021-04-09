# Рекурсивные строки.

def main():
    # Начинаем:
    i = 1
    # Заканчиваем:
    n = int(input('Количество строк: '))

    stars(i, n)

def stars(i, n):

    if i <= n:
        print(i * '*')
        return stars(i + 1, n)

main()