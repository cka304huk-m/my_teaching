import random
a = random.randint(0, 12)
print('a =', a)
b = 1

if a < 10:
    b = 0
    print("a меньше 10, b теперь =", b)
else:
    b = 99
    print("a больше 10, b теперь =", b)