age = int(input("Введите ваш возраст: "))

if age <= 1:
    print("Младенец")
elif age > 1 and age < 13:
    print("Ребенок")
elif age >= 13 and age <= 20:
    print("Подросток")
elif age > 20:
    print("Взрослый")
else:
    print("Как такое возможно.")