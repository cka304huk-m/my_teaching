# Напишите фрагмент кода, который извлекает и
# расконсервирует словарь, законсервированный в задании 11.

import pickle

with open('mydata.dat', 'rb') as data:

    dct = pickle.load(data)

data.close()

print(dct)