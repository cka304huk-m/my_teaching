class Beverage:
    def __init__(self, bev_name):
        self.__bev_name = bev_name

    def get_name_beverage(self):
        return self.__bev_name

class Cola(Beverage):
    def __init__(self):
        Beverage.__init__(self, 'кока-кола')

beverage = Beverage('Напиток')
cola = Cola()
print(beverage.get_name_beverage())
print()
print(cola.get_name_beverage())