deposited_amount = float(input("Сумма которую хотите внести с начала: "))
annual_interest_rate = float(input("Годовая процентная ставка: "))
annual_interest_rate = annual_interest_rate / 100
interest_rate = float(input("Как часто будет начислятся процент: "))
number_of_years = float(input("Количество лет, в течении которых я буду получать доход: "))

full = deposited_amount * (1 +(annual_interest_rate / interest_rate)) ** (interest_rate * number_of_years)
print("C суммы в", deposited_amount, "вы заработаете", format(full, ",.2f"))