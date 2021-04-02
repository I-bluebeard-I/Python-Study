"""
5. * (вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же,
значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
  {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
"""


import os
from pprint import pprint

research_dir = 'C:\Windows'
statistics = {
      100: [0, []],
      1000: [0, []],
      10000: [0, []],
      100000: [0, []],
      1000000: [0, []],
      10000000: [0, []],
      100000000: [0, []],
      10000000000000: [0, []],
    }
key_list = []


for key in statistics.keys():
    key_list.append(key)

for file in os.listdir(research_dir):
    path = os.path.join(research_dir, file)
    if os.path.isfile(path):
        try:
            extensions = file[file.rindex('.') + 1:]
        except ValueError:
            break

        for val in range(len(key_list)):
            if os.stat(path).st_size <= key_list[val]:
                statistics[key_list[val]][0] += 1
                statistics[key_list[val]][1].append(extensions)
                statistics[key_list[val]][1].sort()
                break

pprint(statistics, width=100)
