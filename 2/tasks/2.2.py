SALES = 10 / 100
price = float(input("Цена: "))
full_price = (price) * SALES
print("С учётом скидки ", SALES, '% цена составит $', full_price, sep='')