# Класс Question.

class Question:

    # Атрибуты.
    def __init__(self,
                 question='',
                 answer='',
                 num_correct_answer=''):
        self.question = question
        self.answer = answer
        self.num_correct_answer = num_correct_answer

    def get_question(self):
        # Получаю вопрос.
        return self.question

    def get_answers(self):
        # Варианты ответов.
        return self.answer

    def get_correct_answer(self):
        # Правильный ответ.
        return self.num_correct_answer