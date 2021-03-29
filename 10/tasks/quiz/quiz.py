# Импортирую словарь с вопросами
# и ответами.
from dict_question import quest
# Импортирую класс для обработки вопросов.
from question import Question

def main():
    # Сохраняю 2 словаря с вопросами
    # 1 игроку и 2 игроку.
    quest_p1, quest_p2 = question_player(quest)

    # Сохраняю в переменных очки за правильные ответы.
    point1 = quiz_player(quest_p1, 1)
    point2 = quiz_player(quest_p2, 2)

    # Нахожу победителя.
    winner(point1, point2)


def quiz_player(quest, num):
    """Викторина"""

    # Счетчик вопросов.
    count_quesrion = 1

    # Счетчик правильных ответов:
    correct_answer = 0

    print('Игроку №', num, ' приготовиться!', sep='')
    print()
    # Перебираю словарь чтобы получить
    # с него ключ и значения.
    for k, val in quest.items():
        q = Question(k, val)
        print('Вопрос №', count_quesrion, sep='')
        print(q.get_question())
        print('Варианты ответа:')
        # Перебираю список с ответами.
        for v in q.get_answers()[0:4]:
            print(v)
        # Пустая сторока.
        print()
        answer = int(input('Ваш ответ: '))
        # Сравниваю ответ пользователя с последним
        # значением в списке(это правильный ответ).
        if answer == q.get_answers()[-1]:
            print('Правильно')
            print()
            correct_answer += 10
            count_quesrion += 1
        else:
            print('Ошибочка вышла.')
            print()
            count_quesrion += 1

    return correct_answer

def question_player(dict_quest):
    """Вопросы для игроков."""

    # Вопросы 1 игроку.
    dict_player1 = {}
    # Вопросы 2 игроку.
    dict_player2 = {}
    # Перебираю словарь.
    for k, v in dict_quest.items():
        # Если длина словаря dict_player1 < 5.
        if len(dict_player1) < 5:
            # Сохраняю вопросы с ответами
            # для 1 игрока.
            dict_player1[k] = v
        # Иначе.
        else:
            # Сохраняю вопросы с ответами
            # для 2 игрока.
            dict_player2[k] = v

    return dict_player1, dict_player2

def winner(point1, point2):
    """Определение победителя викторины"""
    print()
    print('Игрокам было задано по 5 вопросов.')
    print('Игрок №1 заработал', point1, 'очков.')
    print('Игрок №2 заработал', point2, 'очков.')
    print()
    if point1 == point2:
        print('У нас ничья.')
    elif point1 > point2:
        print('Победил 1 игрок.')
    elif point1 < point2:
        print('Победил 2 игрок.')

main()