# Эта программа создает экзепляр класса SavingAccount
# и экзепляр класса CD.

import accounts

def main():
    # Получить номер счёта, процентную ставку,
    # и остаток сберегательного счёта.
    print('Введите данные о сберегательном счёте.')
    acct_num = input('Номер счёта: ')
    int_rate = float(input('Процентная ставка: '))
    balance = float(input('Остаток: '))

    # Создать объект SavingAccount.
    savings = accounts.SavingAccount(acct_num, int_rate,
                                     balance)

    # Получить номер счёта, процентную ставку,
    # остаток счёта и дату погашения счёта CD.
    print('Введите данные о счете CD.')
    acct_num = input('Номер счёта: ')
    int_rate = float(input('Процентная ставка: '))
    balance = float(input('Остаток: '))
    maturity = input('Дата погашения: ')

    # Создать объект CD.
    cd = accounts.CD(acct_num, int_rate, balance, maturity)

    # Показать введенные данные.
    print('Вот введеные Вами данные:')
    print()
    print('Сберегательный счёт')
    print('-------------------')
    print('Номер счёта:', savings.get_account_num())
    print('Процентная ставка:', savings.get_interest_rate())
    print('Остаток: $', format(savings.get_balance(), '.2f'),
          sep='')
    print('Счёт депозитного сертификата (СD)')
    print('---------------------------------')
    print('Номер счёта:', cd.get_account_num())
    print('Процентная ставка:', cd.get_interest_rate())
    print('Остаток: $',
          format(cd.get_balance(), '.2f'),
          sep='')
    print('Дата погашения:', cd.get_maturity_date())

# Вызвать главную функцию.
main()