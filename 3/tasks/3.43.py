massa_packet = int(input('Введите массу пакета: '))

# сумма за пакет
price = 0

if massa_packet <= 200:
    price = 150
elif massa_packet > 200 and massa_packet <= 600:
    price = 300
elif massa_packet > 600 and massa_packet <= 1000:
    price = 400
elif massa_packet > 1000:
    price = 475
print("Сумма за пакет массой", str(massa_packet) + 'г. составляет', str(price) + ".")