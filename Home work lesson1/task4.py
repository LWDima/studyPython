# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

print('Введите номер четверти: ')
quarter = int(input())
if quarter == 1:
    print('Диапазон возможных координат I четверти: (x > 0), (y > 0)')
if quarter == 2:
    print('Диапазон возможных координат II четверти: (x < 0), (y > 0)')
if quarter == 3:
    print('Диапазон возможных координат III четверти: (x < 0), (y < 0)')
if quarter == 4:
    print('Диапазон возможных координат IV четверти: (x > 0), (y < 0)')
else:
    print('Всего существует 4 четверти, проверьте правильность ввода')
