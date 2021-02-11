# Импортирую модуль для построения круговой диаграмы
import matplotlib.pyplot as plt

def main():
    """Основная функция."""

    r_file = read_file()
    construction_diagram(r_file)


def read_file():
    """Считаываю данные из файла в пустой список."""

    # Пустой список для записи расходов за прошлый месяц.
    expenses = []

    # Читаю файл.
    with open('expenses_last_month.txt', 'r') as last_month:

        # Перебираю файл и заношу данные из него в список
        # предварительно удалив символ новой строки.
        for last in last_month:
            expenses.append(last.rstrip("\n"))

    # Закрываю файл.
    last_month.close()

    # Возвращаю список с расходами за прошлый месяц.
    return expenses

def construction_diagram(expenses):
    """Принимаю от список в качестве аргумента и строю
    круговую диаграмму."""

    # Список расходов.
    exp = expenses

    # Список меток для долей в круговой диаграмме.
    slice_labels = ['Арендная плата', 'Бензин', 'Продукты питания',
                    'Одежда', 'Платежи по автомашине', 'Прочие']

    # Создать из этих значений круговую диаграмму.
    plt.pie(exp, labels=slice_labels)

    # Добавить заголовок.
    plt.title('Расходы за прошлый месяц.')

    # Показать круговую диаграмму.
    plt.show()

main()