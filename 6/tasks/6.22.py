import calendar
# генеарция шагов
import random
# Среднее число шагов.

# Глобальная константы
YEAR = 365 # кол-во дней в году.

# Кол-во дней в месяце.
January = calendar.monthrange(2021, 1)[1]
February = calendar.monthrange(2021, 2)[1]
March = calendar.monthrange(2021, 3)[1]
April = calendar.monthrange(2021, 4)[1]
May = calendar.monthrange(2021, 5)[1]
June = calendar.monthrange(2021, 6)[1]
July = calendar.monthrange(2021, 7)[1]
August = calendar.monthrange(2021, 8)[1]
September = calendar.monthrange(2021, 9)[1]
October = calendar.monthrange(2021, 10)[1]
November = calendar.monthrange(2021, 11)[1]
December = calendar.monthrange(2021, 12)[1]

def main():
    # Основная функция.
    print(
        """
        Меню:
        1 - подготовить файл с кол-вом шагов за 1 год(365 дней)
        2 - Вывести среднее кол-во шагов в каждом месяце.
        """
    )

    choice = int(input('Ваш выбор - '))

    if choice == 1:
        gen_steps()
    elif choice == 2:
        steps_mount()
    else:
        print('Такого пункта нет в меню.')

def gen_steps():
    # Генерация шагов за 1 год(365 дней)

    # Создаю счётчик строк
    count = 0

    # Открываю файл для записи случайного кол-ва
    # шагов за 1 год(365 дней).
    steps = open('steps.txt', 'w')

    # Использую цикл чтобы записать шаги в файл.
    while count != YEAR:
        step = random.randint(1, 10000)
        steps.write(str(step) + "\n")
        count += 1

    # Закрываю файл.
    steps.close()

def steps_mount():
    # Среднее кол-во шагов сделаных в течении месяца.

    # Переменные для записи среднего кол-во шагов
    # за каждый месяц.
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0
    total5 = 0
    total6 = 0
    total7 = 0
    total8 = 0
    total9 = 0
    total10 = 0
    total11 = 0
    total12 = 0

    # Открываю файл в режиме чтения.
    year_steps = open('steps.txt', 'r')

    # Переменная для подсчёта строк в файле.
    count_strings = 0

    while count_strings != YEAR:
        count_strings += 1
        if count_strings <= January:
            total1 += int(year_steps.readline())
        elif count_strings <= (January + February):
            total2 += int(year_steps.readline())
        elif count_strings <= (January + February + March):
            total3 += int(year_steps.readline())
        elif count_strings <= (January + February + March + April):
            total4 += int(year_steps.readline())
        elif count_strings <= (January + February + March + April +
        May):
            total5 += int(year_steps.readline())
        elif count_strings <= (January + February + March + April +
        May + June):
            total6 += int(year_steps.readline())
        elif count_strings <= (January + February + March + April +
        May + June + July):
            total7 += int(year_steps.readline())
        elif count_strings <= (January + February + March + April +
        May + June + July + August):
            total8 += int(year_steps.readline())
        elif count_strings <= (January + February + March + April +
        May + June + July + August + September):
            total9 += int(year_steps.readline())
        elif count_strings <= (January + February + March + April +
        May + June + July + August + September + October):
            total10 += int(year_steps.readline())
        elif count_strings <= (January + February + March + April +
        May + June + July + August + September + October +
        November):
            total11 += int(year_steps.readline())
        elif count_strings <= (January + February + March + April +
        May + June + July + August + September + October +
        November + December):
            total12 += int(year_steps.readline())
    print('Среднее количество шагов.\n')
    print('За Январь -',total1 // January)
    print('За Февраль -',total2 // February)
    print('За Март -', total3 // March)
    print('За Апрель -', total4 // April)
    print('За Май -',total5 // May)
    print('За Июнь -', total6 // June)
    print('За Июль', total7 // July)
    print('За Август', total8 // August)
    print('За Сентябрь', total9 // September)
    print('За Октябрь -', total10 // October)
    print('За Ноябрь -',total11 // November)
    print('За Декабрь -',total12 // December)

# Вызываю главную функцию.
main()