# Найти сумму чисел списка стоящих на нечетной позиции

import random

a = [random.randint(1, 10)for i in range(6)]
print(a)
resul = list(map(lambda x: a[x] if x % 2 == 1 else None, list(range(len(a)))))
resul = sum([i for i in resul if i != None])
print(resul)
