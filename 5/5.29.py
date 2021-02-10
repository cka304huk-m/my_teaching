# Список простых чисел.
def main():
    # Основная функция.
    for i in range(2, 101):
        print(i, '-', is_prime(i))

def is_prime(digit):
    """Определиние простостого числа."""
    if digit % 2 == 0 or digit % 3== 0 or digit % 5 == 0 or digit % 7== 0:
        text = 'простое'
    else:
        text = 'составное'
    return text

# Вызываю основную функцию.
main()