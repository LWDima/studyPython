# Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)

import random

num = int(input('Введите длинну строки: '))
a = [random.randint(1, 10) for i in range(num)]
result = [a[i]*a[-i-1] for i in range(len(a)//2+len(a) % 2)]
print(a)
print(result)
