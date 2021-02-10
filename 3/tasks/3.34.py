# Введите число, а я сконвертирую его в римскую цифру

digit = int(input("Введите число от 1 до 10: "))

if digit == 1:
    print(digit, "= I")
elif digit == 2:
    print(digit, "= II")
elif digit == 3:
    print(digit, "= III")
elif digit == 4:
    print(digit, "= IV")
elif digit == 5:
    print(digit, "= V")
elif digit == 6:
    print(digit, "= VI")
elif digit == 7:
    print(digit, "= VII")
elif digit == 8:
    print(digit, "= VIII")
elif digit == 9:
    print(digit, "= IX")
elif digit == 10:
    print(digit, "= X")
else:
    print("Ошибка вы ввели число больше 10 или меньше 1")