# Лотерея PowerBall.
# Не доделано:
# 10 наиболее "созревших" чисел (чисел, которые не использовались
# долгое время),
# упорядоченных от наиболее созревших до наименее созревших;
# частоту каждого числа от 1 до 69 и частоту каждого PowerBall
# числа от 1 до 26.

# Импортирую модуль чтобы сгенерировать числа
# и записать их в файл.
import random

def main():
    """Основная функция."""

    print(
        """
        Меню:
        1 - Сгенерировать числа в файл(*при повторном запуске
        числа дописываются в файл).
        2 - 1О наиболее распространенных чисел
        3 - 1О наименее распространенных чисел
        """
    )

    num_list, coun_list = frequent_numbers(read_file())
    num_list2, coun_list2 = uncirculated_numbers(read_file())

    choice = int(input('Сделайте выбор: '))
    if choice == 1:
        gen_nun_powerBall()
    elif choice == 2:
        for i in range(len(num_list)):
            print('Число', num_list[i], 'выпадало:', coun_list[i], 'раз(а).')
    elif choice == 3:
        for i in range(len(num_list2)):
            print('Число', num_list2[i], 'выпадало:', coun_list2[i], 'раз(а).')

def gen_nun_powerBall():
    """Генерирую 5 чисел в диапазоне от 1 до 69 и
    генерирую число 'PowerBall' от 1 до 26.
    После чего записываю данные в файл."""

    # Список куда буду сохранять числа
    # которые получу при генерации.
    gen_num = []

    # Генерирую 5 чисел от 1 до 69
    # и записываю в список gen_num.
    while len(gen_num) != 5:
        gen = random.randint(1, 69)
        if gen not in gen_num:
            gen_num.append(gen)

    # Генерирую число 'PowerBall'
    # от 1 до 26.
    powerball = random.randint(1, 26)
    gen_num.append(powerball)

    # Перебираю список и записываю цифры
    # переменную.
    str_gen = ''

    for g in gen_num:
        str_gen += str(g) + " "

    # Удаляю лишний пробел в конце.
    str_gen = str_gen.rstrip()

    # Записываю данные в файл.
    with open('pbnumbers.txt', 'a') as pbnumbers:
        pbnumbers.write(str_gen + "\n")

    # Закрываю файл.
    pbnumbers.close()

def read_file():
    """Чтение данных из файла."""

    # Читаю файл.
    with open('pbnumbers.txt', 'r', encoding='utf-8') as pbnumbers:

        # Сохраняю в список строку.
        list_pb = pbnumbers.read().split()

        # Переменная для посчёта индекса.
        count_index = 0

        # Перевожу символы в списке из строковых
        # в целые.
        for l in list_pb:
            list_pb[count_index] = int(l)
            count_index += 1

    # Закрывю файл.
    pbnumbers.close()

    return list_pb

def frequent_numbers(pb):
    """1О наиболее распространенных чисел, упорядоченных по частоте."""

    # Испортированный список с числами.
    list_pb = pb

    # Список для чисел
    num_list = []

    # Сколько раз число из num_list повторяется.
    coun_list = []

    # Перебираю испортированый список.
    for p in sorted(list_pb):
        if list_pb.count(p) > 1:
            if p not in num_list:
                num_list.append(p)
                coun_list.append(list_pb.count(p))

    # Списки для упорядочевания чисел.
    num_list2 = []
    coun_list2 = []

    # Индекс масимального числа.
    index_count = 0

    # Ищу в списке coun_list максимальное число
    # это повторения числа в списке.

    # Цикл работает пока длина списка coun_list не
    # будет равна 0.
    while len(coun_list) != 0:

        # Нахожу индекс максимального числа.
        index_count = coun_list.index(max(coun_list))

        # Записываю в новый список число с
        # наибольшим количеством повторений.
        num_list2.append(num_list[index_count])

        # Записываю в новый список количество
        # повторений числа с наибольшим повторением.
        coun_list2.append(coun_list[index_count])

        # Удаляю числа по индексу из старых списков.
        del num_list[index_count]
        del coun_list[index_count]

    # Возвращаю первые 10 чисел.
    return num_list2[:10], coun_list2[:10]

def uncirculated_numbers(pb):
    """1О наименее распространенных чисел, упорядоченных по частоте."""

    # Испортированный список с числами.
    list_pb = pb

    # Список для чисел
    num_list = []

    # Сколько раз число из num_list повторяется.
    coun_list = []

    # Перебираю испортированый список.
    for p in sorted(list_pb):
        if p not in num_list:
            num_list.append(p)
            coun_list.append(list_pb.count(p))

    # Списки для упорядочевания чисел.
    num_list2 = []
    coun_list2 = []

    # Индекс минимального числа.
    index_count = 0

    # Ищу в списке coun_list минимальное число
    # это повторения числа в списке.

    # Цикл работает пока длина списка coun_list не
    # будет равна 0.
    while len(coun_list) != 0:

        # Нахожу индекс минимального числа.
        index_count = coun_list.index(min(coun_list))

        # Записываю в новый список число с
        # наименьшим количеством повторений.
        num_list2.append(num_list[index_count])

        # Записываю в новый список количество
        # повторений числа с наименьшим повторением.
        coun_list2.append(coun_list[index_count])

        # Удаляю числа по индексу из старых списков.
        del num_list[index_count]
        del coun_list[index_count]

    # Возвращаю первые 10 чисел.
    return num_list2[:10], coun_list2[:10]

main()
