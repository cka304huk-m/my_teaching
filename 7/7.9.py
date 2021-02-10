def main():
    # Пустой список.
    list_numbers = []

    repeat = 'д'

    while repeat == 'д':
        # Спрашиваю числа, а потом их сохраняю в список.
        num = float(input('Число: '))
        list_numbers.append(num)
        repeat = input('Повторить д = да, все остальное = нет: ')

    print('Минимальное число:', min(list_numbers))
    print('Максимальное число:', max(list_numbers))

    total = 0

    for numbers in list_numbers:
        total += numbers
    print('Сумма чисел в списке:', total)

    mean_num = total / len(list_numbers)
    print('Среднее арифмитеское:', mean_num)

main()