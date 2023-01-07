# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите число: '))
lst = [n]


def multi(lst):
    fl = 0
    for i in range(lst[-1] // 2, 1, -1):
        if lst[len(lst)-1] % i == 0:
            lst.append(i)
            lst[-2] = lst[-2] // i
            fl += 1

    if fl != 0:
        multi(lst)


multi(lst)

print(lst)
