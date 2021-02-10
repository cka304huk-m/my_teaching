import random

def main():
    for l in gen_numbers():
        print(l, end=' ')

def gen_numbers():
    # Генерирует числа для лотерейных билет,
    # которые я сохранию в список
    DIGIT = 7

    loto = [0] * DIGIT
    repeat = 0
    # Применяю цикл для генерации случайных чисел.
    while repeat < DIGIT:
        dig = random.randint(1, 9)
        if dig not in loto:
            loto[repeat] = dig
            repeat += 1

    return loto

main()