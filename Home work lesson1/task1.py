# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

print('Введи число обозначающее день недли: ')
num = int(input())
if num >= 6 and num <= 7:
    print(num, 'Этот день выходной ')
elif num >= 1 and num <= 5:
    print(num, 'Этот день рабочий ')
else:
    print(num, 'Такого дня не существует')
