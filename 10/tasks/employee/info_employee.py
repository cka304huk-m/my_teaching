import employee

def main():

    worker0 = employee.Employee('Сьюзан Мейерс',
                                '47899', 'Бухгалтерия',
                                'Вице-президент')
    worker1 = employee.Employee('МаркДжоунс',
                                '39119', 'ИТ', 'Программист')
    worker2 = employee.Employee('Джой Роджерс', '81774',
                                'Производственный', 'Инженер')

    print('[Имя         ][ИД   ][Отдел    ][Должность   ]')
    print(worker0)
    print(worker1)
    print(worker2)


main()