"""
4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), размер
которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""


import os
from pprint import pprint

research_dir = './'
statistics = {
      100: 0,
      1000: 0,
      10000: 0,
      100000: 0,
      1000000: 0,
      10000000: 0
    }
key_list = []


for key in statistics.keys():
    key_list.append(key)

for file in os.listdir(research_dir):
    path = os.path.join(research_dir, file)
    if os.path.isfile(path):
        for val in range(len(key_list)):
            if os.stat(path).st_size <= key_list[val]:
                statistics[key_list[val]] += 1
                break

pprint(statistics, width=20)
