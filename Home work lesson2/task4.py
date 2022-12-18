# Задайте список из N элементов, заполненных числами из промежутка
# [-N, N]. Найдите произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке одно число.

a = int(input('Введите число n: '))
index = input(
    'Введите индексы элементов, произведение кторорых надо вычислить: ').split()
index_int = list(map(int, index))

list = []
result = 1

for i in range(a, 0, -1):
    list.append(i*-1)
for i in range(0, a+1, 1):
    list.append(i)

for i in range(len(index_int)):
    result *= list[index_int[i]]

print(list)
print(index_int)
print(result)
