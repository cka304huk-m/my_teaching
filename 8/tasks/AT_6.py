# Напишите фрагмент кода, делающий копию
# строкового значения, в котором все вхождения
# буквы 'т' в нижнем регистре преобразованы в
# верхний регистр.

my_string = 'Теремок в лесу, Только эТо все сказка.'

new_string1 = ''
new_string2 = ''

for s in my_string:
    if 'т' in s.lower():
        new_string1 += s.lower()
    else:
        new_string1 += s

print('Новая строка:', new_string1)

for s in my_string:
    if s.lower() == 'т':
        new_string2 += s.replace('Т', 'т')
    else:
        new_string2 += s

print('Еще вариант:', new_string2)
