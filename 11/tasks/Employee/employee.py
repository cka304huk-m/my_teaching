# Класс 'Сотрудник'.
class Employee:

    # Атрибуты.
    def __init__(self, name, id):
        self.__name_employee = name
        self.__id_employee = id

    # Методы-модификатор.
    def set_name(self, name):
        self.__name_employee = name

    def set_id(self, id):
        self.__id_employee = id

    # Методы получатели.
    def get_name(self):
        return self.__name_employee

    def get_id(self):
        return self.__id_employee

# Класс 'Рабочий'.
class ProductionWorker(Employee):

    # Наследования атрибутов из класса
    # родителя Employee
    def __init__(self, name, id, shift_num, rate):
        Employee.__init__(self, name, id)

        # Атрибуты класса.
        self.__shift_number = shift_num
        self.__rate_hourly = rate

    # Методы-модификаторы.
    def set_shift_num(self, sn):
        self.__shift_number = sn

    def set_rate_hourly(self, rate):
        self.__rate_hourly = rate
    
    # Методы-получатели.
    def get_shift_num(self):
        if self.__shift_number == 1:
            return 'дневную смену'
        elif self.__shift_number == 2:
            return 'ночную смену'

    def get_rate_hourly(self):
        return self.__rate_hourly

# Класс 'Начальник смены'.
class ShiftSupervisor(Employee):

    # Атрибуты класса родителя(наследования).
    def __init__(self, name, id, salary, bonus):
        Employee.__init__(self, name, id)

        # Атрибуты подкласса ShiftSupervision.
        self.__annual_salary = salary
        self.__production_bonus = bonus

    # Методы-модификаторы.
    def set_annual_salary(self, salary):
        self.__annual_salary = salary

    def set_production_bonus(self, bonus):
        self.__production_bonus = bonus

    # Методы-получатели.
    def get_annual_salary(self):
        return self.__annual_salary

    def get_production_bonus(self):
        return self.__production_bonus