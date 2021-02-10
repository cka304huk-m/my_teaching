number_of_shares = 2000
kp_sum_share_one = 40.00
pr_sum_share_one = 42.75
broker_commission = 0.03
print("На покупку", format(number_of_shares, ','), "акций, Джо потратил:")
kp_ak_and_sum_one = number_of_shares * kp_sum_share_one
kp_broken = kp_ak_and_sum_one * broker_commission
all_kp = kp_ak_and_sum_one + kp_broken
print("\t- сумма за акции:", kp_ak_and_sum_one)
print("\t- комиссия брокера в 3%:", kp_broken)
print("Итого:", all_kp)

print("\n\nНа продаже", format(number_of_shares, ","), "акций, Джо заработал:")
pr_ak_and_sum_one = number_of_shares * pr_sum_share_one
pr_broken = pr_ak_and_sum_one * broker_commission
all_pr = pr_ak_and_sum_one + pr_broken
print("\t- сумма за акции:", pr_ak_and_sum_one)
print("\t- комиссия брокера в 3%:", pr_broken)
print("Итого:", all_pr)

print("\nЧистый доход составил:", all_pr - all_kp)