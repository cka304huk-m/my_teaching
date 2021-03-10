# Нахождение простого числа.

a, b = input().split()
a = int(a)
b = int(b)
# Перебираю числа от а до b.
if 0 < a < b < 100000:
    for num in range(a, b):
        # Cчетчик делителей.
        count = 0
        delitel = 2
        while delitel < num:
            if num % delitel == 0:
                count += 1
            delitel += 1
        if count == 0:
            print(num)
