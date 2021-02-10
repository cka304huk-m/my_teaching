# Основные цвета, которые не возможно получить
# путём смешивания
red = 'красный'
blue = 'синий'
yellow = 'желтый'

color1 = input("Первый цвет: ")
color2 = input("Второй цвет: ")

if (color1 == red and color2 == blue) or \
        (color2 == red and color1 == blue):
    print("При смешивании", color1, 'и',
          color2, "мы создали новый цвет - 'фиолетовый'")
elif (color1 == red and color2 == yellow) or (color1 == yellow and color2 == red):
    print("При смешивании", color1, 'и',
          color2, "мы создали новый цвет - 'оранжевый'")
elif (color1 == blue and color2 == yellow) or \
        (color1 == yellow and color2 == blue):
    print("При смешивании", color1, 'и',
          color2, "мы создали новый цвет - 'зеленый'")
else:
    print("Ошибка!")