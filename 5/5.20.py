# Футы в дюймы.

# Глобальные константы.
FUT = 12    # 1 фут = 12 дюймам.

def main():
    # Основная функция.
    f = int(input('Количество футов: '))
    print(f, 'фут(ов) = ', feer_to_inches(f), 'дюйм(а/ов).')


def feer_to_inches(futs):
    return futs * FUT

main()