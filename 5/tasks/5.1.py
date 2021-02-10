def main():
    digit = int(input('Целое число: '))
    print('Число', digit, 'умноженное на 10 =', times_ten(digit))

def times_ten(digit):
    return digit * 10

main()