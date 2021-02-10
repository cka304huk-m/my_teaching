# Цена 1 программы в рознице
PROGRAM_PRICE = 99

# вводим сколько хотим купить пакетов програм.
sales = int(input("Сколько купим пакетов программ: "))

# Проверяем условие и на основании него решаем давать ли скидку.
if sales >= 10 and sales <= 19:
    discount = sales * 0.1
    my_sales = (sales * PROGRAM_PRICE) - discount
    print("За покупку", sales, 'вы получили скидку в 10%.')
    print("Сумма со скидкой составляет", my_sales)
elif sales >= 20 and sales <= 49:
    discount = sales * 0.2
    my_sales = (sales * PROGRAM_PRICE) - discount
    print("За покупку", sales, 'вы получили скидку в 20%.')
    print("Сумма со скидкой составляет", my_sales)
elif sales >= 50 and sales <= 99:
    discount = sales * 0.3
    my_sales = (sales * PROGRAM_PRICE) - discount
    print("За покупку", sales, 'вы получили скидку в 30%.')
    print("Сумма со скидкой составляет", my_sales)
elif sales >=100:
    discount = sales * 0.4
    my_sales = (sales * PROGRAM_PRICE) - discount
    print("За покупку", sales, 'вы получили скидку в 40%.')
    print("Сумма со скидкой составляет", my_sales)
else:
    print("У вы, но скидка на", sales, 'пакет(ов) пограммы не предпологается.')
    my_sales = sales * PROGRAM_PRICE
    print('Сумма за программы составляет:', my_sales)