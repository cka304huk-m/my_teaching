# Класс Information.
class Information:

    # Атрибуты.
    def __init__(self, name, address, age, telephone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__number_telephone = telephone

    # Методы получатели.
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_num_telephone(self):
        return self.__number_telephone

    # Методы модификаторы.
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_num_telephone(self, telephone):
        self.__number_telephone = telephone