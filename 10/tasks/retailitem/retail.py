import retailitem

def main():
    for _ in range(1, 4):
        product = input('Описание: ')
        quantity = input('Количество на складе: ')
        price = float(input('Цена: '))

        print('-' * 61)
        print('|', ' ' * 8, '|', 'Описание', ' ' * 2, \
              '|', 'Количество на складе', ' ' * 2, '|', \
              'Цена ', '|')
        print('-' * 61)

        my_retail = retailitem.RetailItem(product, quantity, price)
        print('|Товар №,', _, end='')
        print('|', my_retail.get_description(), " " * (11 - len(my_retail.get_description())), end='')
        print('|', my_retail.get_quantity(), ' ' * (23 - len(my_retail.get_quantity())), end='')
        print('|', my_retail.get_price(), '|')
        print('-' * 61)

main()