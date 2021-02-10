my_seconds = int(input("Введите кол-во секунд: "))

DAY = 86400    # секунд в 1 дне
HOUR = 3600   # секунд в 1 часе
MINUTA = 60 # секунд в 1 минуте

#Преобразовывываем секунды в часы, минуты, дни
if my_seconds >= 60 and my_seconds < 3600:
    minutes = my_seconds // MINUTA
    seconds = my_seconds % MINUTA
    print(my_seconds, 'секунда(ы) =', minutes, 'минуте(ам) и',
          seconds, 'секунде(ам).')
elif my_seconds >= 3600 and my_seconds < 86400:
    hours = my_seconds // HOUR
    minutes = my_seconds // MINUTA % MINUTA
    seconds = my_seconds % MINUTA
    print(my_seconds, "секунда(ы) =", hours, 'часам(ов)',
          minutes, 'минуте(ам) и', seconds, 'секунде(ам).')
elif my_seconds >= 86400:
    days = my_seconds // DAY
    hours = my_seconds // HOUR - 24
    minutes = my_seconds // MINUTA % MINUTA
    seconds = my_seconds % MINUTA
    print(my_seconds, "секунда(ы) =",
          days, "дню(ям)",
          hours, 'часам(ов)',
          minutes, 'минуте(ам) и', seconds, 'секунде(ам).')
else:
    seconds = my_seconds
    print(my_seconds, 'секунда(ы) =', seconds, 'секунде(секундам)')