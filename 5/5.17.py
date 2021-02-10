# Сидячие места на стадионе.

# Глобальные константы.
A_M = 20
B_M = 15
C_M = 10

def main():
    # Основная функция
    a = int(input('А мест продано: '))
    b = int(input('B мест продано: '))
    c = int(input('С мест продано: '))
    print('Мы заработали:', all_price(a, b, c))

def all_price(a, b, c):
    """Считаем наши заработки."""
    return a * A_M + b * B_M + c * C_M

main()