# Класс 'Человек'.
class Person:

    def __init__(self, name, address, telephone):
        self.__name = name
        self.__address = address
        self.__telephone = telephone

    # Методы-модификаторы.
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_telephone(self, telephone):
        self.__telephone = telephone

    # Методы-получатели.
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_telephone(self):
        return self.__telephone

# Класс 'Клиент', который является подклассом
# класса 'Person'.
class Customer(Person):

    # Атрибуты которые наследую из класса
    # родителя 'Person'.
    def __init__(self, telephone, yes_no):
        # Применяю полиморфизм чтобы не передавать атрибуты: name,
        # address в класс 'Customer'.
        Person.__init__(self, 'петя иванов', 'москва сити', telephone)

        # Атрибуты класса 'Customer'.
        self.__yes_no = yes_no

    # Методы-модификаторы.
    def set_yes_no(self, yn):
        self.__yes_no = yn

    # Методы-получатели.
    def get_yes_no(self):
        if self.__yes_no.lower() == 'да':
            return 'клиент хочет получать рекламные новости.'
        elif self.__yes_no.lower() == 'нет':
            return 'клиент нехочет получать рекламные новости.'
        else:
            return 'Вы допустили ошибку при вводе.'