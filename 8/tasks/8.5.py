# Алфавитный переводчик номера.

def main():
    """Основная функция."""

    print("Введите номер в таком формате: 555-GET-FOOD")
    input_number = input('Номер:')
    print('Номер в цирах таков:', decode_number_digit(input_number))

def decode_number_digit(num):
    """Декодирую буквенный номер в цифры."""

    # Сохраняю номер в переменную.
    number = num

    # Номер в цифрах.
    num_digit = ''

    # Перебираю номер.
    for n in number:
        n = n.upper()
        if n == 'A' or n == 'B' or n == 'C':
            num_digit += '2'
        elif n == 'D' or n == 'E' or n == 'F':
            num_digit += '3'
        elif n == 'G' or n == 'H' or n == 'I':
            num_digit += '4'
        elif n == 'J' or n == 'K' or n == 'L':
            num_digit += '5'
        elif n == 'M' or n == 'N' or n == 'O':
            num_digit += '6'
        elif n == 'P' or n == 'Q' or n == 'R' or n == 'S':
            num_digit += '7'
        elif n == 'T' or n == 'U' or n == 'V':
            num_digit += '8'
        elif n == 'W' or n == 'X' or n == 'Y' or n == 'Z':
            num_digit += '9'
        else:
            num_digit += n

    # Возвразаю цифровой номер.
    return num_digit

# Вызываю основную функцию.
main()