import person

def main():

    telepehone = input('Номер телефона: ')
    yn = input('Получать новости на телефон? да/нет ')

    # Создаю экземпляр клиента.
    customer = person.Customer(telepehone, yn)
    print()
    print('Номер телефона', customer.get_telephone())
    print(customer.get_yes_no())

main()