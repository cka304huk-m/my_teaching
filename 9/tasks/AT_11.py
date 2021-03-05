# Предположим, что переменная dct ссылается на словарь.
# Напишите фрагмент кода, который консервирует словарь
# и сохраняет его в файле mydata.dat.

import pickle

dct = {'Майк': 'Нью Йорк', 'Владимир': 'Москва'}

with open('mydata.dat', 'wb') as mydata:

    pickle.dump(dct, mydata)

mydata.close()