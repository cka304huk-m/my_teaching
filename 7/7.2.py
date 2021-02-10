# Общий объем продаж.

# Дней в недели
WEEK = 7

def main():
    print('Сумма продаж за неделю:', total_sale(sales_input()))


def sales_input():

    # Список продаж
    sales_week = [0] * WEEK

    for index in range(WEEK):
        print('Введите продажи за ', index + 1, ': ',
              sep='', end='')
        sales_week[index] = float(input())

    return sales_week

def total_sale(total):

    dig_total = 0

    for num in total:
        dig_total += num
    return dig_total

main()