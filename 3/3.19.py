import random

speed = random.randint(-250, 250)

if speed < 0 or speed > 200:
    print("Число", speed, 'не лежит в диапазоне от 0 до 200')
else:
    print("Число", speed, 'лежит в диапазоне от 0 до 200')