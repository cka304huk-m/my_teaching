# Класс Procedure.

class Procedure:

    # Атрибуты класса.
    def __init__(self, name, date, doctor, cost):
        self.__name_procedure = name
        self.__date_procedure = date
        self.__name_doctor_performed_procedure = doctor
        self.__cost_procedure = cost

    # Методы получатели.
    def get_name_procedure(self):
        return self.__name_procedure

    def get_date_procedure(self):
        return self.__date_procedure

    def get_name_doctor_performed_procedure(self):
        return self.__name_doctor_performed_procedure

    def get_cost_procedure(self):
        return self.__cost_procedure

    # Методы модификаторы.
    def set_name_procedure(self, name):
        self.__name_procedure = name

    def set_date_procedure(self, date):
        self.__date_procedure = date

    def set_name_doctor_performed_procedure(self, doctor):
        self.__name_doctor_performed_procedure = doctor

    def set_cost_procedure(self, cost):
        self.__cost_procedure = cost