# Класс Bank.
class Bank:

    # Атрибуты класса.
    def __init__(self, account, percent):
        self.__account = account
        self.__percent = percent

    # Методы модификаторы.
    def add_account(self, account):
        # Добавления суммы на счёт.
        self.__account += account

    def set_percent(self, percent):
        # Установить процент.
        self.__percent = percent

    def del_account(self, account):
        if account <= self.__account:
            self.__account -= account
        else:
            print('На счёте меньше денег!')
            print(self.get_account())

    # Методы получатели.
    def get_account(self):
        return self.__account

    def get_percent(self):
        return self.__percent