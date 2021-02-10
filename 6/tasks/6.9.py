try:
    x = float('abc123')
    print('Конвертация завершена.')
except IOError:
    print('Этот программный код вызвал ошибку IOError.')
except ValueError:
    print('Этот командный код вызвал ошибку ValueError.')
print('Конец')