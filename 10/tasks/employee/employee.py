# Класс Employee.
class Employee:

    # Атрибуты.
    def __init__(self, name, id, division, function):
        self.__name = name
        self.__id_number = id
        self.__division = division
        self.__function = function

    # Методы получатели.
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id_number

    def get_division(self):
        return self.__division

    def get_function(self):
        return self.__function

    def __str__(self):
        return self.__name + ' ' + self.__id_number + ' ' + \
               self.__division + ' ' +  self.__function