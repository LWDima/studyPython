# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


k = int(input('Введите число -> '))
a = randint(0, 100)
b = randint(0, 100)
c = randint(0, 100)
with open('Home work lesson4/task4/task4_4.txt', 'w', encoding='utf-8') as file:
    file.write(f'{a}*x^{k} + {b}*x + {c} = 0')
