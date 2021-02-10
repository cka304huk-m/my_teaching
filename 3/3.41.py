buying_books = int(input('Сколько книг вы купите в этом месяце: '))
points = 0
if buying_books == 0:
    points = 0
elif buying_books == 2:
    points = 5
elif buying_books == 4:
    points = 15
elif buying_books == 6:
    points = 30
elif buying_books >= 8:
    points = 60
print('За покупку', buying_books, 'книг, вы заработали', points, 'очков.')