# Вес
weight = float(input())
# Рост
growth = float(input())
# Результат
result = weight / (growth * 2)

if result < 18.5:
    print('Недостаточный вес')
elif result >= 18.5 and result <= 25:
    print('Нормальный')
elif result >= 25 and result <= 30:
    print('Избыточный вес')
elif result >= 30:
    print('Ожирение')