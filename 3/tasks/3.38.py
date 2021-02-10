PACK_SAUSASES = 10  # упаковка сосисок
PACK_BUNS = 8       # упаковка булочек

number_of_picnic_participants = int(input('Кол-во учасников: '))
number_of_hot_dogs = int(input("Кол-во хот догов: "))

# Узнаю сколько всего нужно хот догов
total_hot_dogs = number_of_picnic_participants * number_of_hot_dogs
print("\nВсего необходимо -", total_hot_dogs, 'хот догов.')

# Узнаю кол-во упаковок с сосисками
packs_sausases = total_hot_dogs // PACK_SAUSASES
remainder_sauses = total_hot_dogs % PACK_SAUSASES
print("\tДля этого понадобится", packs_sausases, "упаковки и", remainder_sauses, "шт. сосисок.")

# Узнаю кол-во упаковок булочек
packs_buns = total_hot_dogs // PACK_BUNS
remainder_buns = total_hot_dogs % PACK_BUNS
print("\tДля этого понадобится", packs_buns, "упаковки и", remainder_buns, "шт. булочек.")