tuition_fees = 45000    # Плата за обучения семестр
raising = 0.03          # увеличение на 3% каждый год

for i in range(1, 6):
    if i == 1:
        print('За', i, 'год плата за 1 семетр составит', format(tuition_fees, '.2f'))
    else:
        tuition = tuition_fees * raising
        tuition_fees += tuition
        print('За', i, 'год плата за 1 семетр составит', format(tuition_fees, '.2f'))