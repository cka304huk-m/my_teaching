class Plant:
    def __init__(self, plant_type):
        self.__plant_type = plant_type
    def message(self):
        print('Я - планета.')

class Tree(Plant):
    def __init__(self):
        Plant.__init__(self, 'дерево')
    def message(self):
        print('Я - дерево.')

p = Plant('Саженец')
t = Tree()
p.message()
t.message()