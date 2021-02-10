import random

amount1 = random.randrange(201)
amount2 = random.randrange(201)
print("amount1 =", amount1, "\tamount2 =", amount2)

if amount1 > 10 and amount2 < 100:
    if amount1 > amount2:
        print("amount1 =", amount1, "\tamount2 =", amount2)
    else:
        print("amount2 =", amount2, "\tamount1 =", amount1)