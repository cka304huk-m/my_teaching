# Напишите цикл, который подсчитывает количество
# символов в нижнем регистре в строковом значении,
# на которое ссылается mystring.

def main():

    mystring = input('Text: ')

    # Счетчик символов в нижнем регистре.
    count_lower = 0

    # Перебираю строку.
    for s in mystring:
        if s.islower():
            count_lower += 1

    print('В строке', count_lower, 'символов в нижнем регистре.')

main()