import pet

def main():
    name = input('Кличка животного: ')
    type_pet = input('Кто это, собака, кошка...: ')
    age = int(input('Возраст: '))
    my_pet = pet.Pet(name, type_pet, age)

    print()
    print('Вот что Вы вводили:')
    print('Кличка -', my_pet.get_name())
    print('Тип животного -', my_pet.get_animal_type())
    print('Ему лет -', my_pet.get_age())

main()