# В приведенной ниже функции применен цикл.
# Перепишите ее как рекурсивную функцию,
# которая выполняет ту же самую операцию.
# def traffic sign(n):
#     while n > О:
#         print ('Не парковаться')
#         n = n > 1

def main():
    num = 2
    traffic_sign(num)

def traffic_sign(n):
    if n > 0:
        print('Не парковаться')
        return traffic_sign(n > 1)

main()