import information

def main():
    neo = information.Information('Томас А. Андерсон', 'Матрица',
                                25, '+1-985-*****')
    morpheus = information.Information('Морфеус', 'Матрица',
                                33, '+1-986-*****')

    trinity = information.Information('Тринити', 'Матрица',
                                       29, '+1-987-****')

    print('Вымышленая информация о героях фильма матрица:')
    print('Имя:', neo.get_name())
    print('Адрес:', neo.get_address())
    print('Возраст:', neo.get_age())
    print('Телефон:', neo.get_num_telephone())
    print()
    print('Имя:', morpheus.get_name())
    print('Адрес:', morpheus.get_address())
    print('Возраст:', morpheus.get_age())
    print('Телефон:', morpheus.get_num_telephone())
    print()
    print('Имя:', trinity.get_name())
    print('Адрес:', trinity.get_address())
    print('Возраст:', trinity.get_age())
    print('Телефон:', trinity.get_num_telephone())

main()