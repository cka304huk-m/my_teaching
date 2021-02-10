# Расчет калорий за счёт жиров и углеводов.

def main():
    """Основная функция"""
    fat = float(input('Количество жиров: '))
    carbohydrates = float(input('Количество углеводов: '))
    print('Калорий от жиров:', kal_fat(fat))
    print('Калорий от углеводов:', kal_carbohydrates(carbohydrates))

def kal_fat(f):
    return f * 9

def kal_carbohydrates(c):
    return c * 4

main()