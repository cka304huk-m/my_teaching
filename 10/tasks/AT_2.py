# Напишите определение класса с именем вооk.
# Класс Book должен иметь атрибуты данных
# для заголовка книги, имени автора и имени издателя.
# Этот класс должен также иметь
# следующие методы:
# • метод _ init _ () для класса должен принимать аргумент
# для каждого атрибута данных;
# • методы-получатели и методы-модификаторы для каждого атрибута
# данных;
# • метод _ str_ (), который возвращает строковое значение,
# сообщающее о состоянии объекта.

# Класс Book
class Book:

    # Атрибуты класса.
    def __init__(self, title, author, publisher):
        self.__title_book = title
        self.__author_book = author
        self.__publisher = publisher

    # Методы модификаторы.
    def set_title(self, title):
        self.__title_book = title

    def set_author(self, author):
        self.__author_book = author

    def set_publisher(self, publisher):
        self.__publisher = publisher

    # Методы получатели.
    def get_title(self):
        return self.__title_book

    def get_author(self):
        return self.__author_book

    def get_publisher(self):
        return self.__publisher

    # Метод возвращающий строковое значение.
    def __str__(self):
        return 'Книга: ' + self.__title_book + \
    '\nАвтор: ' + self.__author_book + \
            '\nИздатель: ' + self.__publisher

book = Book('Весь Шерлок Холмс', 'Артур Конан Дойл',
            'Петроглиф, Амфора')
print(book)