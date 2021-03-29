"""
5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать путь к обоим
исходным файлам и путь к выходному файлу со словарём. Проверить работу скрипта для случая, когда все файлы находятся
в разных папках.
"""

import sys
import os

for arg in sys.argv[1:3]:
    if os.path.exists(arg) == False or len(sys.argv) < 4:

        print('\nДля работы программы наберите:\n'
                'PYTHON <имя скрипта.PY> <файл входных данных 1> <файл входных данных 2> <файл вывода>')
               # python part01_lesson06_task05.py data/users.csv data/hobbys.csv data/outdata.csv
        exit(0)

users_data = sys.argv[1]
hobbys_data = sys.argv[2]
out_data = sys.argv[3]
user_dict = {}

with open(users_data, 'r', encoding='utf-8') as users, \
     open(hobbys_data, 'r', encoding='utf-8') as hobbys, \
     open(out_data, 'a', encoding='utf-8') as out_data:
    while True:
        user_tmp = users.readline().strip()
        user_line = user_tmp.split(',')
        if user_tmp:
            while True:
                hobby_tmp = hobbys.readline().strip()
                hobby_line = hobby_tmp.split(',')
                if not hobby_tmp:
                    user_dict[tuple(user_line)] = None
                else:
                    user_dict[tuple(user_line)] = tuple(hobby_line)
                print(user_dict.popitem(), file=out_data)
                break
        elif hobby_tmp != '':
            exit(1)
        else:
            break
