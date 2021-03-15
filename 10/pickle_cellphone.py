# Эта программа консервирует объекты CellPhone.
import pickle
import cellphone

# Константа для имени файла.
FILENAME = 'cellphone.dat'

def main():
    # Инициализиировать переменную для управления циклом.
    again = 'д'

    # Открыть файл.
    with open(FILENAME, 'wb') as output_file:

        # Получить данные от пользователя.
        while again.lower() == 'д':
            # Получить данные о сотовом телефоне.
            man = input('Введите производителя: ')
            mod = input('Введите номер модели: ')
            retail = float(input('Введите розничную цену: '))

            # Создать объект CellPhone.
            phone = cellphone.CellPhone(man, mod, retail)

            # Законсервировать объект и записать его в файл.
            pickle.dump(phone, output_file)

            # Получить еще один элемент данных?
            again = input('Введёте еще один элемент данных? (д/н): ')

    # Закрыть файл.
    output_file.close()
    print('Данные записаны в', FILENAME)

# Вызвать главную функцию.
main()