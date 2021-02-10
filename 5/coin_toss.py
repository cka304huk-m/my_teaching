# Эта программа имитирует 10 бросков монеты.
import random

# Константы.
HEADS = 1       # Орёл
TAILS = 2       # Решка.
TOSSES = 10     # Количество бросков.

def main():
    for toss in range(TOSSES):
        # Имитировать бросание монеты.
        if random.randint(HEADS, TAILS) == HEADS:
            print('Орёл')
        else:
            print('Решка')

# Вызвать главную функцию.
main()