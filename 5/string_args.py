# Эта программа демонстрирует передачу в функцию двух
# строковых аргументов.

def main():
    first_name = input('Ваше имя: ')
    last_name = input('Ваша фамилия: ')
    print('Ваше имя в обратном порядке')
    reverse_name(first_name, last_name)

def reverse_name(first, last):
    print(last, first)

# Вызвать главную функцию.
main()