# Генератор персональной страницы.
"""
1. Импортировать модуль для переименования файла.
2.Запросить у пользователя данные.
а) Введите свое имя.
б) Опишите себя.
3. Открыть файл для записи данных.
4. Записать в него теги
5. Добавить информацию пользователя.
6. Записать теги.
7. Закрыть файл.
8. Переименовать файл, дать ему новое расширение.
"""
# Модуль для переименования файла.
import os

def main():
    name = input('Введите свое имя: ')
    description = input('Опишите себя: ')

    # Открываю файл в режиме записи.
    my_page = open('page.txt', 'w')

    # Записываю в файл теги.
    my_page.write('<html>\n')
    my_page.write('<head>\n')
    my_page.write('</head>\n')
    my_page.write('<body>\n')
    my_page.write('\t<center>\n')
    my_page.write('\t<h1>')
    my_page.write(name)
    my_page.write('</h1>\n')
    my_page.write('\t</center>\n')
    my_page.write('\t<hr />\n')
    my_page.write("\t")
    my_page.write(description)
    my_page.write("\n")
    my_page.write('\t<hr />\n')
    my_page.write('</body>\n')
    my_page.write('</html>\n')

    # Закрываю файл.
    my_page.close()

    # Переименовываю его в веб страницу.
    os.rename('page.txt', 'my_page.html')

main()