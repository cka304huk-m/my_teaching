# Проверка допустимости номера расходноrо счета.

def main():

    scores_list = []

    score = input('Счёт: ')

    # Название файла
    file = 'charge_accounts.txt'

    # Прочитать данные из файла.
    with open(file, 'r') as account:
        charge = account.readline()

        while charge !='':
            scores_list.append(charge.rstrip("\n"))
            charge = account.readline()

    if score in scores_list:
        print('Номер допустимый')
    else:
        print('Номер недопустимый')


    account.close()

main()