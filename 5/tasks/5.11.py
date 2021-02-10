# Преобразование километров в мили

def main():
    km = float(input('Сколько км вы проехали: '))
    print(km, "климетров =", format(km_in_mili(km), '.1f'), 'милям.')

def km_in_mili(km):
    return km * 0.6214

main()