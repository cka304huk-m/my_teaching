# Принтер дат. Напишите программу, которая считывает
# от пользователя строковое значение, содержащее дату
# в формате дд/мм/гггг. Она должна напечатать дату в формате
# 12 марта 2018 г.

def main():
    """Основная функция."""
    data = get_data()
    data_now = get_mount(data)

    print(data_now[0], data_now[1], data_now[2], 'г.')

def get_mount(data):

    list_data = data.split('/')
    if list_data[1] == '1' or list_data[1] == '01':
        list_data[1] = 'Января'
    elif list_data[1] == '2' or list_data[1] == '02':
        list_data[1] = 'Февраля'
    elif list_data[1] == '3' or list_data[1] == '03':
        list_data[1] = 'Марта'
    elif list_data[1] == '4' or list_data[1] == '04':
        list_data[1] = 'Апреля'
    elif list_data[1] == '5' or list_data[1] == '05':
        list_data[1] = 'Мая'
    elif list_data[1] == '6' or list_data[1] == '06':
        list_data[1] = 'Июня'
    elif list_data[1] == '7' or list_data[1] == '07':
        list_data[1] = 'Июля'
    elif list_data[1] == '8' or list_data[1] == '08':
        list_data[1] = 'Августа'
    elif list_data[1] == '9' or list_data[1] == '09':
        list_data[1] = 'Сентября'
    elif list_data[1] == '10':
        list_data[1] = 'Октября'
    elif list_data[1] == '11':
        list_data[1] = 'Ноября'
    elif list_data[1] == '12':
        list_data[1] = 'Декабря'

    return list_data

def get_data():

    # Текущая дата
    data_now = ''

    day = input('День: ') + "/"
    mount = input('Месяц: ') + "/"
    year = input('Год: ')

    data_now = day + mount + year

    return data_now

# Вызываю основную функцию.
main()