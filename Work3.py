#Задайте словарь из n чисел последовательности
# (1 + (1/n))^n и выведите на экран их сумму.

n = int(input('Введите число: '))

dict = {}
sum = 0

for i in range(1, n+1):
    dict [i] = round((1 + (1/i))**i,2)
    sum +=dict[i]

print (f'Словарь: {dict}')
print(f'Сумма значений словаря: {round(sum,2)}')