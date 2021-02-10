import random

A_SCORE = 95
B_SCORE = 85
C_SCORE = 75
D_SCORE = 65

score = random.randrange(100)
print("score =", score)

if score >= A_SCORE:
    print("Ваш уровень - A.")
else:
    if score >= B_SCORE:
        print("Ваш уровень - B.")
    else:
        if score >= C_SCORE:
            print("Ваш уровень - C.")
        else:
            if score >= D_SCORE:
                print("Ваш уровень - D.")
            else:
                print("Ваш уровень - F.")
