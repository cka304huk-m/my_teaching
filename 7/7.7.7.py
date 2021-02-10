# Экзамен на получение водительских прав.

def main():
    # Поиск позиции в списке.
    index = 0
    # Правильные ответы.
    good = 0
    for student in student_answer():
        if student == good_answer()[index]:
            print(index + 1, ": ", good_answer()[index], '- правильно.')
            good += 1
        index += 1
    if good >= 15:
        print('Вы прошли экзамен, неправильных вопросов:', 20 - good)
    else:
        print('Вас ожидает пересдача, неправильных вопросов:', 20 - good)


def good_answer():
    """Считываю правильные ответы из файла и заношу их в список"""

    # Создаю список в который буду складывать
    # правильные ответы
    g_answer = []

    # Считываю файл с правильными ответами.
    with open('student_solution.txt', 'r') as answer:

        # Прохожу файл циклом и записываю все в список.
        for a in answer:
            g_answer.append(a.rstrip("\n"))

    # Закрываю файл.
    answer.close()
    return g_answer

def student_answer():
    """Считываю ответы студента из файла и заношу их в список"""

    # Создаю список в который буду складывать
    # правильные ответы
    s_answer = []

    # Файл из которого считываю ответы студента.
    filename = 'student_solution2.txt'

    # Читаю файл с ответами.
    with open(filename, 'r') as answer:

        # Прохожу файл циклом и записываю все в список.
        for a in answer:
            s_answer.append(a.rstrip("\n"))

    # Закрываю файл.
    answer.close()
    return s_answer

main()