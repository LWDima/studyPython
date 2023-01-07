# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('Home work lesson4/task5/doc1.txt', 'r') as file:
    mnog1 = file.read()
    mnog1 = mnog1[0:-4]

with open('Home work lesson4/task5/doc2.txt', 'r') as file:
    mnog2 = file.read()

with open('Home work lesson4/task5/sum.txt', 'w', encoding='utf-8') as file:
    file.write(f'{mnog1} + {mnog2}')
