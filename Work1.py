num = input('Введите число: ')

sum = 0

for i in num:
    if i != '.':
        sum += int(i)

print(f'Сумма цифр в числе равна {sum}')
