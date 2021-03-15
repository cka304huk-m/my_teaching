# Эта программа передает объект Coin
# в качестве аргумента функцию.
import coin

# Главная функция.
def main():
    # Создать объект Coin.
    my_coin = coin.Coin()

    # Эта инструкция покажет 'Орёл'.
    print(my_coin.get_sideup())

    # Передать объект в функцию flip.
    flip(my_coin)

    # Эта инструкция может показать 'Орёл'
    # либо 'Решка'.
    print(my_coin.get_sideup())

# Функция flip подбрасывает монету.
def flip(coin_obj):
    coin_obj.toss()

# Вызвать главную функцию.
main()