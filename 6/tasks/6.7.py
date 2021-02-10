# Модуль для удаления и переименования.
import os

def main():
    # Создать булевую переменную.
    found = False

    # Переменная с именем студента которого нужно удалить.
    bad_student = 'Jon Perc'

    # Открываю файл students.txt в режиме чтения.
    students = open('students.txt', 'r')

    # Открываю файл temp.txt в режиме записи.
    temp = open('temp.txt', 'w')

    # читаю певою строку файла.
    my_stud = students.readline()

    while my_stud != '':
        # Прочитать оценку студента
        appraisal = float(students.readline())

        # Удаляем новую строку из имени.
        my_stud = my_stud.rstrip('\n')

        # Проверяем есть ли в файле студент для отчисления,
        # если его нет в списке то записываем его во временный
        # файл.
        if my_stud != bad_student:
            temp.write(my_stud + "\n")
            temp.write(str(appraisal) + "\n")
        else:
            # Назначить флагу found значение True.
            found = True

        # Прочитать следующего студента из файла.
        my_stud = students.readline()

    # Закрыть файл со списком студетов.
    students.close()

    # Закрыть временный файл.
    temp.close()

    # Удаляем исходный файл.
    os.remove('students.txt')

    # Переименовываем файл temp.txt в students.txt.
    os.rename('temp.txt', 'students.txt')

    # Если студент был найден, то показать сообщение.
    if found:
        print('Студент отчислен.')
    else:
        print('Нет такого студента.')

# Вызываю функцию.
main()