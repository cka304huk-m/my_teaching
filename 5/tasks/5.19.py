# Месячный налог с продаж

# Глобальные константы
FED_NALOG = 0.05
MUN_NALOG = 0.025

def main():
    # Основная функция
    all_price = float(input('Общий объем продаж: '))
    print('Сумма муниципального налога с продаж:', mun(all_price))
    print('Сумма федерального налога с продаж:', fed(all_price))
    print('Общий налог с продаж (муниципальный плюс федеральный):',
          all(all_price))

def mun(price):
    return price * MUN_NALOG

def fed(price):
    return price * FED_NALOG

def all(price):
    return mun(price) + fed(price)

main()