# Класс Patient.

class Patient:

    # Атрибуты
    def __init__(self, name, address, telephone, contact):
        self.__name_patronymic_surname = name
        self.__address_city_region_zip = address
        self.__number_telephone = telephone
        self.__name_telephone_emergency = contact

    # Методы получатели.
    def get_name_patronymic_surname(self):
        return self.__name_patronymic_surname

    def get_address_city_region_zip(self):
        return self.__address_city_region_zip

    def get_number_telephone(self):
        return self.__number_telephone

    def get_name_telephone_emergency(self):
        return self.__name_telephone_emergency

    # Методы модификаторы.
    def set_name_patronymic_surname(self, name):
        self.__name_patronymic_surname = name

    def set_address_city_region_zip(self, address):
        self.__address_city_region_zip = address

    def set_number_telephone(self, telephone):
        self.__number_telephone = telephone

    def set_name_telephone_emergency(self, contact):
        self.__name_telephone_emergency = contact