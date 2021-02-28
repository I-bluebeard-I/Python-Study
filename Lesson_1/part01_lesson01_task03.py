"""
ЗАДАНИЕ 3

Сумма чисел из списка *
Создать список, состоящий из кубов нечётных чисел от 0 до 1000 (куб X - третья степень числа X):

1) Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!

2) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из нового списка,
сумма цифр которых делится нацело на 7.

3) Написать алгоритм вычисляющий то же значение суммы, что и в пункте 2), но не создавая списков
"""

sum_total = 0

# Создать список, состоящий из кубов нечётных чисел от 0 до 1000
numbers = [num for num in range(1, 10 ** 3 + 1)]
numbers = list(filter(lambda x: x % 2,
              map(lambda x: x ** 3, numbers)))

# 1. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7
for number in numbers:                                  # для каждого числа в списке
    sum_of_digit = 0
    for digit in str(number):                           # для каждой цифры в числе
        sum_of_digit += int(digit)
    if sum_of_digit % 7 == 0:
        sum_total += number
print(f'1. {sum_total}')

# 2. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из нового списка,
# сумма цифр которых делится нацело на 7.
sum_total = 0
numbers_2 = []

for number in numbers:
    numbers_2.append(number + 17)
for number in numbers_2:                                # для каждого числа в списке
    sum_of_digit = 0
    for digit in str(number):                           # для каждой цифры в числе
        sum_of_digit += int(digit)
    if sum_of_digit % 7 == 0:
        sum_total += number
print(f'2. {sum_total}')

# 3. Алгоритм вычисляющий то же значение суммы, что и в пункте 2), но не создавая списков
sum_total = 0
number = 5

while number < 1000:
    if number % 2 != 0:                                 # если число не четное возводим в куб + смещение 17
        cube_number = number ** 3 + 17
        sum_of_digit = 0
        while cube_number != 0:
            sum_of_digit += (cube_number % 10)
            cube_number //= 10
        if sum_of_digit % 7 == 0:
            sum_total += (number ** 3 + 17)
    else:
        pass
    number += 1
print(f'3. {sum_total}')
