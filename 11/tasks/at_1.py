class Dog:
    # Класс Dog.

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

class Poodle(Dog):

    def __init__(self, name):
        Dog.__init__(self, name)

# Создаю экзепляры: Dog, Poodle
dog = Dog('Шавка')
poodle = Poodle('Артымон')
print(dog.get_name())
print()
print(poodle.get_name())