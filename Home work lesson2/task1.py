# # Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# # Пример:
# # - 6782 -> 23
# # - 0,56 -> 11ф

#

a = input('Введите любое вещественное число: ')


def summ(x):
    if float(x) < 0:
        x = float(x) * (-1)
    number = 0

    for i in str(x):
        if i != '.':
            number += int(i)
    return number


print(f'Сумма чисел равна {summ(a)}')
