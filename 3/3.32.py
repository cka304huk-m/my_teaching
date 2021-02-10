# Узнаем параметры 1 прямоугольника
length1 = float(input("Длина прямоугоника №1: "))
width1 = float(input("Ширина прямоугольника №1: "))

# Площадь первого прямоугольника
areaRectangle1 = length1 * width1
print("Площадь прямоугольника №1 =", areaRectangle1)

# Узнаем параметры 2 прямоугольника
length2 = float(input("Длина прямоугоника №2: "))
width2 = float(input("Ширина прямоугольника №2: "))

# Площадь первого прямоугольника
areaRectangle2 = length2 * width2
print("Площадь прямоугольника №2 =", areaRectangle2)

if areaRectangle1 == areaRectangle2:
    print("Прямоугольники равны")
elif areaRectangle1 > areaRectangle2:
    print("Прямоугольник №1, больше пряугольника №2")
elif areaRectangle1 < areaRectangle2:
    print("Прямоугольник №2, больше пряугольника №1")
else:
    print("Это не возможно.")