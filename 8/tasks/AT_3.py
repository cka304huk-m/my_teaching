# Напишите цикл, который подсчитывает
# количество цифр в строковом значении,
# на которое ссылается mystring.

def main():

    mystring = input('Text: ')

    # Счетчик кол-ва цифр в строке.
    count_num = 0
    
    # Перебираю строку.
    for s in mystring:
        if s.isdigit():
            count_num += 1
    print('В тексте я обнаружил', count_num, 'цифр')

# Основная функция.
main()