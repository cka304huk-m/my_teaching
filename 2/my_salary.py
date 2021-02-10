# Расчитывает мою зарплату на основании
# потраченых часов
oneHour = 186.92        # Один час моей работы стоит
NDFL = 0.13             # 13% которые уходят в налоговую
NIGHT_PERCENT = 0.0294  # За ночные смены
HARMFULNESS = 0.0373    # За вредность
hours = int(input("Сколько часов ты отработал: "))
full = oneHour * hours              # Основная зарплата
harm = full * HARMFULNESS           # Вредность
night = full * NIGHT_PERCENT        # ночные смены
pens = (full + harm + night) * NDFL # сняли налоговая
all_full = (full + harm + night)
my_sales = (full + harm + night) - pens
print("\nВсего тебе начислили: ₽", format(all_full, '.2f'),
      "\n\tОсновная зараплата: ₽", format(full, ",.2f"),
      "\n\tВредность: ₽", format(harm, ",.2f"),
      "\n\tНочные смены: ₽", format(night, ",.2f"),
      '\n\tПенсионный фонд забрал у тебя: ₽', format(pens, ",.2f"),
      "\nУвы но твоя итоговая зарплата: ₽", format(my_sales, ",.2f"), sep='')
