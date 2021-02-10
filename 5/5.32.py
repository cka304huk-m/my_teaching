# Игра "Камень, ножницы, бумага".

import random   # модуль для генерации выбора пк.

def main():
    # Основная функция.
    user = input_user()
    pc = r_p_s()
    print('Компьютер выбирает:')
    if pc == 1:
        print('Камень')
    elif pc == 2:
        print('Ножницы')
    elif pc == 3:
        print('Бумага')
    print('\nИсход сражения:',battle_user_vs_pc(pc, user))
    if user == pc or pc == user:
        user = input_user()
        pc = r_p_s()
        print('\nИсход сражения:', battle_user_vs_pc(pc, user))



def r_p_s():
    # генерирования случайного значения.
    a = random.randint(1, 3)
    return a

def input_user():
    # ввод пользователя.
    b = input('Ваш выбор: ')
    if b == 'камень' or b == 'Камень':
        b = 1
    elif b == 'ножницы' or b == 'Ножницы':
        b = 2
    elif b == 'бумага' or b == 'Бумага':
        b = 3
    return b

def battle_user_vs_pc(a, b):
    # Тут происходит вся битва.
    text = ''
    if (a == b):
        text = 'ничья'
    elif (a == 1 and b == 2):
        text = 'камень разбивает ножницы - победитель ПК'
    elif (a == 2 and b == 1):
        text = 'камень разбивает ножницы - победитель Пользователь'
    elif (a == 2 and b == 3):
        text = 'ножницы режут бумагу - победитель Пользователь'
    elif (a == 3 and b == 2):
        text = 'ножницы режут бумагу - победитель ПК'
    elif (a == 1 and b == 3):
        text = 'бумага заворачивает камень - победитель Пользователь'
    elif (a == 3 and b == 1):
        text = 'бумага заворачивает камень - победитель ПК'
    return text

main()