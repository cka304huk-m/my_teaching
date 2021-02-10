# Больше числа n.

def main():
    n = n_numbers()
    l_numbers = list_numbers()
    n_list(l_numbers, n)

def n_numbers():
    """Запрашивает у пользователя число."""
    n = int(input('Число: '))
    return n

def list_numbers():
    """Создает список"""
    l_numbers = list(range(1, 45))
    return l_numbers

def n_list(list_numbers, n_numbers):
    """Показывает числа в списке которые больше n"""
    for l in list_numbers:
        if l > n_numbers:
            print(l, '>', n_numbers)

main()