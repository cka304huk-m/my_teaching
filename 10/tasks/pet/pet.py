# Класс Pet.
class Pet:
    # Аргументы животного.
    def __init__(self, name, type, age):
        self.__name = name
        self.__animal_type = type
        self.__age = age

    # Методы модификации.
    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, type):
        self.__animal_type = type

    def set_age(self, age):
        self.__age = age

    # Методы получатели.
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age