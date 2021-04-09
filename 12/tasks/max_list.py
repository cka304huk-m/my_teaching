# Максимальное значение в списке.

def main():
    # Список значений.
    num_list = [23, 2423, 1234, 23, 765]

    print(max_num(num_list))

def max_num(num):
    # Если длина списка = 1.
    if len(num) == 1:
        # Вывожу первое значение.
        return num[0]
    # Иначе использую функцию max для поиска 
    # максимальных значений в списке.
    else:
        return max(num[0], max_num(num[1:]))
    
main()