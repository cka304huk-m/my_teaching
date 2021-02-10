pocket_number = int(input("Введите номер кармана: "))

if pocket_number >= 0 and pocket_number <= 36:
    if pocket_number == 0:
        print('Зеленый')
    elif pocket_number >= 1 and pocket_number <=10:
        if pocket_number == 1 \
                or pocket_number == 3 \
                or pocket_number == 5 \
                or pocket_number == 7 \
                or pocket_number == 9:
            print('Красный')
        else:
            print('Черный')
    elif pocket_number >= 11 and pocket_number <= 18:
        if pocket_number == 11 \
            or pocket_number == 13 \
            or pocket_number == 15 \
            or pocket_number == 17:
            print("Черный")
        else:
            print('Красный')
    elif pocket_number >= 19 and pocket_number <= 28:
        if pocket_number == 19 \
            or pocket_number == 21 \
            or pocket_number == 23 \
            or pocket_number == 25 \
            or pocket_number == 27:
            print('Красный')
        else:
            print('Черный')
    elif pocket_number >= 29 and pocket_number <= 36:
        if pocket_number == 29 \
            or pocket_number == 31 \
            or pocket_number == 33 \
            or pocket_number == 35:
            print('Черный')
        else:
            print('Красный')
else:
    print(pocket_number, "не находиться в диапазоне от 0 до 36.")