# Эта программа демоснстрирует класс BankAccount.

import bankaccount

def main():
    # Получить начальный остаток.
    start_bal = float(input('Введите свой начальный остаток: '))

    # Создать объект BankAccount.
    savings = bankaccount.BankAccount(start_bal)

    # Внести на счёт зарплату пользователя.
    pay = float(input('Сколько Вы получили на этой неделе? '))
    print('Вношу эту сумму на Ваш счёт.')
    savings.deposit(pay)

    # Показать остаток.
    print('Ваш остаток на банковском счёте составляет ₽',
          format(savings.get_balance(), '.2f'),
          sep='')

    # Получить сумму для снятия с банковского счёта.
    cash = float(input('Какую сумму вы желаете снять со счёта? '))
    print('Снимаю эту сумму с Вашего банковского счёта.')
    savings.withdraw(cash)

    # Показать остаток.
    print('Ваш остаток на банковском счёте составляет ₽',
          format(savings.get_balance(), '.2f'),
          sep='')

# Вызвать главную функцию.
main()