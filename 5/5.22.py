# Правильно не правильно.

def main():
    """Основная функция."""
    answer = input('Столица России: ')
    print(answer_to_the_question(answer))

def answer_to_the_question(answer):
    """Проверка правильный ли ответ дал пользователь."""
    if answer == 'москва' or answer == 'Москва':
        return 'Молодец, да столица России - это Москва!'
    else:
        return 'Извини, но столица России - это Москва!'

main()