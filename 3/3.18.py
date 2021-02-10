import random

speed = random.randint(1, 300)
print(speed)

if speed >= 0 and speed <= 200:
    print("Число", speed, "лежит в диапазоне от 0 до 200")
else:
    print('Число', speed, 'не лежит в диапазоне от 0 до 200')