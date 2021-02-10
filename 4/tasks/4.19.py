# Повышения уровеня океана в год
ocean_level_age = 1.6 # мм
print('Год Уровень')
print('-----------')
for i in range(1, 26):
    print(' ',i, '  ', format(i * ocean_level_age, '.1f'), 'мм. в год.', sep='')