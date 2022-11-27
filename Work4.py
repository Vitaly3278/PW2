# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

n = int(input('Введите количество элементов: '))

numbers = []
res = 1

for i in range(n):
    numbers.append(randint(-n, n + 1))
print(f'Список элементов: {numbers}\n')

#num = int(input('Введите количество позиций для записи: '))  # сделал с записью позиций элементов в файл

#data = open('file.txt', 'w')
#for i in range(num):
#    elem = input('Введите индекс элемента для записи: ')
#    data.write(elem + '\n')
#data.close()

data = open('file.txt', 'r')
for line in data:
    res *= numbers[int(line)]
data.close()

print(f'Произведение элементов: {res}')
