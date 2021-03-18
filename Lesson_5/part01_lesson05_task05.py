"""
5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список с
сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
"""


from time import perf_counter

source = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []
repeat = []

start = perf_counter()
for pos, num in enumerate(source):
    repeat = list(1 for pos2, num2 in enumerate(source) if pos2 != pos and num == num2)
    if len(repeat) == 0:
        result.append(num)
    repeat = []
print(result, perf_counter() - start)       # 6,41936E-05 среднее время выполнения


"""
start = perf_counter()
for pos, num in enumerate(source):
    for pos2, num2 in enumerate(source):
        if pos2 != pos:
            if num == num2:
                repeat = 1
                break
    if repeat == 0:
        result.append(num)
    repeat = 0
print(result)
print(perf_counter() - start)               # 7,6993E-05 среднее время выполнения
"""