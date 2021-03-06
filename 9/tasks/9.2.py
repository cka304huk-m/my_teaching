# Викторина со столицами.

# Модуль для выбора случайной страны из словаря.
import random

def main():
    """Основная функция."""

    contry = country_capital()

    choice = ''
    while choice != '0':
        quiz_counrys(contry)
        choice = input('Для выхода - 0, для продолжения любая клавиша: ')

def quiz_counrys(contry):
    """Узнаю у пользователя какая столица загаданной страны."""
    conceived = choice_country(contry)

    # Счетчики правильных и не правильных ответов.
    correct_count = 0
    wrong_count = 0

    print('Я загадала страну:', conceived)
    answer = ''
    while answer != contry[conceived]:
        answer = input('А её столица: ')
        if answer in contry[conceived]:
            print('Вы правы столица', conceived, '- это', contry[conceived])
            correct_count += 1
        else:
            print('Не правильно!')
            wrong_count += 1
            print('Еще раз, столица', conceived)
            answer = input('- ')
    print('Правильных ответов:', correct_count)
    print('Не правильных ответов:', wrong_count)

def choice_country(country):
    """Выбирает случайным образом страну и её столицу."""

    # В список записываю случайную страну.
    enigmatic_country = []

    # Генератор случайной цифры
    num_key = random.randrange(len(country))
    # Счетчик для сверки со случайным числом.
    count = 0

    for c in country.keys():
        if count == num_key:
            if len(enigmatic_country) < 1:
                enigmatic_country.append(c)
        else:
            count += 1


    return enigmatic_country[0]

def country_capital():
    """Словарь со странами и их столицами."""

    county = {
        'Россия': 'Москва',
        'Руанда': 'Кигали',
        'Румыния': 'Бухарест',
        'Сальвадор': 'Сан - Сальвадор',
        'Саудовская Аравия': 'Эр-Рияд',
        'Северная Корея': 'Пхеньян',
        'Сербия': 'Белград',
        'Сирия': 'Дамаск',
        'Словакия': 'Братислава',
        'Словения': 'Любляна',
        'Соединенные Штаты Америки': 'Вашингтон',
    }

    return county

main()