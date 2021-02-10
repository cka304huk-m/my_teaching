def main():
    numbers = list(range(1, 11))
    print('Сумма чисел в списке =',get_list_total(numbers))

def get_list_total(num):
    total = 0
    for n in num:
        total += n
    return total

main()