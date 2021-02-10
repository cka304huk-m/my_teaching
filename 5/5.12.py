# Вычисления налога с продаж

# Константы с налогами
REGn = 0.05         # 5 %
FEDn = 0.13         # 13%

def main():
    # Главная функция
    prices = float(input("Сумма продаж: "))

    my_prices = prices - (reg_nalog(prices) + fed_nalog(prices))
    print('Всего мы заработали: ₽', prices, sep='')
    print('Но у нас ушло на налоги:')
    print('Региональный: ₽', format(reg_nalog(prices), '.2f'), sep='')
    print('Федеральный: ₽', format(fed_nalog(prices), '.2f'), sep='')
    print('За вычитом всех налогов мы заработали: ₽', my_prices, sep='')

def reg_nalog(price):
    # Считаем региональный налог
    return price * REGn

def fed_nalog(price):
    # Считаем федеральный налог
    return price * FEDn

# Вызываю главную функцию.
main()
