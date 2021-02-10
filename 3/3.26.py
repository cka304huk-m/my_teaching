import random

speed = random.randrange(100)
print("Текущая скорость =", speed)

if speed >= 24 and speed <= 56:
    print("Скорость нормальная")
else:
    print("Скорость аварийная.")