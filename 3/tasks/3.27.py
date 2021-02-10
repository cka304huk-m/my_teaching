import random

points = random.randrange(60)
print('points =', points)

if points < 9 or points > 51:
    print("недопустимые точки")
else:
    print("Допустимые точки")