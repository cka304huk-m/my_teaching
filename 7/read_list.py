# Эта программа считывает содержимое файла в список.

def main():
    # Открыть файл для чтения.
    with open('cities.txt', 'r') as infile:

        # Прочитать содержимое файла в список.
        cities = []
        for city in infile:
            cities.append(city)

    # Закрыть файл.
    infile.close()

    # Удалить из каждого элемента символ \n.
    index = 0
    while index < len(cities):
        cities[index] = cities[index].rstrip('\n')
        index += 1

    # Напечатать содержимое списка.
    print(cities)

# Вызвать главную функцию.
main()