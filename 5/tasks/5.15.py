# Налог на недвижимое имущество.

ASSESSED_VALUE = 0.6        # Оценочная стоимость 60%
                            # от фактической стоимости.
PRICE_PER_ACRE = 0.0072     # 72 цента с каждой $100

def main():
    # Основная функция.
    price = float(input('Стоимость жилья: '))
    print('Оценочная стоиомость = ', format(asessed(price), '.2f'))
    print('Налог на акры =', format(per_acre(price), '.2f'))

def asessed(price):
    # Оценочная стоимость.
    return price * ASSESSED_VALUE

def per_acre(price):
    # Налог на имущество
    return price * PRICE_PER_ACRE

# Вызываю главную функцию.
main()