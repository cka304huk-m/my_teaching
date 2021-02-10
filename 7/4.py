import re

# Пишем текст в котором будем искать слово.
text = input()

# Пишем слово которое нужно найти в переменной text
word = input()

# re.search(слово, текст)
if re.search(word, text):
    print('Слово найдено')
else:
    print('Слово не найдено')