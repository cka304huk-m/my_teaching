import bank

def main():
    menu()

def menu():
    """Меню."""
    choice = 0

    while choice != 4:
        print(
            """
            Меню:
            1 - Положить на счёт.
            2 - Добавить на счёт.
            3 - Снять деньги со счёта.
            4 - Выход.
            """
        )
        choice = int(input('Ваш выбор: '))
        if choice > 4 or choice < 1:
            choice = int(input('Ваш выбор: '))
        else:
            if choice == 1:
                print()
                deposit = float(input('Сколько положить на счёт: '))
                percent = float(input('Под какой процент: '))
                account_bank = bank.Bank(deposit, percent)
                print('На счету сейчас', account_bank.get_account())
                print('Процент по вкладу = ',
                      account_bank.get_percent(), '%', sep='')
            elif choice == 2:
                try:
                    print()
                    a_account = float(input('Сколько добавить: '))
                    account_bank.add_account(a_account)
                    percent = float(input('Под какой процент: '))
                    account_bank.set_percent(percent)
                    print('Готово, на счету сейчас', account_bank.get_account(),
                          '\nпроцентная ставка по владу: ', account_bank.get_percent())
                except UnboundLocalError:
                    percent = float(input('Под какой процент: '))
                    account_bank = bank.Bank(a_account, percent)
                    print('На счету сейчас', account_bank.get_account())
                    print('Процент по вкладу = ',
                          account_bank.get_percent(), '%', sep='')
            elif choice == 3:
                print()
                print('На счету сейчас', account_bank.get_account())
                d_account = float(input('Сколько снять: '))
                account_bank.del_account(d_account)
                print('На счету осталось ', account_bank.get_account())

main()