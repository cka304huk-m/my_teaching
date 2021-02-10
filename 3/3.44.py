massa_kg = float(input("Сколько ты весишь в кг.: "))
growth_sm = float(input("Твой рост в см.: "))

# расчёт идекса массы тела
imt = massa_kg / ((growth_sm /100) * (growth_sm / 100))
print(format(imt, '.2f'))

if imt >= 18.5 and imt <= 25:
    print('Ваш вес в норме')
elif imt < 18.5:
    print('Ваш вес ниже нормы')
elif imt > 25:
    print("Твой вес привышает норму.")