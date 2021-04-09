# Рекурсивная сумма списка.

def main():
    
    # Генерирую список с числами от 1 до 45.
    numbers = list(range(1, 46))
    # Позиция в списке.
    i = 0
    
    print(amount(numbers, i))

def amount(num, i):
    if i >= len(num):
        return 0
    else:
        return num[i] + amount(num, i + 1)

main()