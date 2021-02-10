weight = float(input("Введите массу тела: "))

# Вычисляю массу тела в ньютонах
summ = weight * 9.8

if summ > 500:
    print("Тело слишком тяжелое")
elif summ < 100:
    print("Тело слишком легкое")