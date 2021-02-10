# -*- coding: cp1251 -*-
# Волшебный шар.

# Импортирую модуль для генерации случайного ответ
import random

def main():
    """Основная часть."""
    print('Задайте свой вопрос, а программа попробует ' \
          'предсказать случиться ли это')

    # Переменная для завершение программы.
    repeat = 'д'

    while repeat.lower() == 'д':
        input_question()
        random_answer = random.choice(read_list_answers())
        print(random_answer)

        # Повторить?
        repeat = input('Д = да, все остальное = нет: ')

def input_question():
    """Принимаю от пользователя вопрос."""

    question = input('Что вас интересует: ')

    # Возвращаю вопрос.
    return  question

def read_list_answers():
    """Читаю список ответов из файла."""

    # Пустой список для сохранения ответов из файла.
    answers = []

    # Читаю файл с ответами.
    with open('8 _ball_responses.txt', 'r', encoding="utf-8") as list_answers:

        # Перебираю файл и сохраняю ответы в список answers,
        # предварительно удалив символ новой строки.
        for ans in list_answers:
            answers.append(ans.rstrip("\n"))

    # Закрываю файл.
    list_answers.close()

    # Возвращаю список с ответами.
    return answers

# Вызываю основную функцию.
main()