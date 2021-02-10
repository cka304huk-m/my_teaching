import random
b = 12
c= 0
print("b =", b, "\tc =", c)
a = random.randint(0, 11)
print("a =", a)
if a < 10:
    b = 0
    c = 1
    print("а меньше 10")
print("b =", b, "\tc =", c)