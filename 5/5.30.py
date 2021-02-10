# Будущая стоимость.

def main():
    # Основная функция.
    current_amount = float(input('Текущая сумма: '))
    monthly_interest_rate = float(input('% ставка в месяц: '))
    monthly_interest_rate /= 100
    mounts_amount = float(input('Количество месяцев: '))
    print('Будущая сумма на счёте будет =',
          format(future_value(current_amount,
                              monthly_interest_rate,
                              mounts_amount), '.2f'))

def future_value(c_a, m_i_r, m_a):
    # Высчитываем будущую стоимость.
    f = c_a * ((1 + m_i_r) ** 2)
    return f

# Вызываю основную функцию.
main()