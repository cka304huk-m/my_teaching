# модуль для удаления и переименования файла.
import os

def main():
    # Булевой флаг для вывода найдет студент
    # или нет.
    found = False

    # Имя студента для изменения оценки.
    name_student = 'Igor Sklyar'
    new_appraisal = 100

    # Открываем оригинальный файл в режиме чтения.
    stud = open('students.txt', 'r')

    # Открываю временный файл в который будет произведена
    # запись новой оценки если студент будет найден.
    temp = open('temp.txt', 'w')

    # Читаю первую строку в оригинальном файле.
    my_stud = stud.readline()

    # Использую цикл чтобы полностью прочитать оригинальный файл.
    while my_stud != '':
        # Получаю оценку.
        appraisal = float(stud.readline())

        # Удаляю \n после имени студента
        my_stud = my_stud.rstrip('\n')

        # Если текущее имя равно имени студента
        if my_stud == name_student:
            temp.write(my_stud + "\n")
            temp.write((str(new_appraisal) + "\n"))
            # Студент найден изменяем значение.
            found = True
        else:
            # Записать исходные оценки в файл
            temp.write(my_stud + "\n")
            temp.write((str(appraisal) + "\n"))

        # Прочитать следующию строку.
        my_stud = stud.readline()

    # Закрыть основной и временный файл.
    stud.close()
    temp.close()

    # Удалить исходный файл
    os.remove('students.txt')

    # Переименовать временный файл.
    os.rename('temp.txt', 'students.txt')

    # Если студент в файле найден, то показать сообщение.
    if found:
        print('Оценка изменена.')
    else:
        print('Нет такого студента.')

# Вызываю главную фунцию.
main()