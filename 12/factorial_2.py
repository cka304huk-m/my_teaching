def fact(x):
    if x == 1:
        return 1
    return fact(x - 1) * x

print(fact(4))
print(fact(10))