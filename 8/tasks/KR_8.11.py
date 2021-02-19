# Напишите фрагмент кода с использованием оператора in,
# который определяет, является ли 'd' подстрокой
# переменной mystring.

def main():

    mystring = input('Write text please: ')

    if 'd' in mystring or 'D' in mystring:
        print('Symbol "d" in mystring')
    else:
        print('Symbol "d" not in mystring')

# Вызываю главную функцию.
main()