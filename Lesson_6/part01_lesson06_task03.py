"""
3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при
хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные
о хобби. Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше
записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». При
решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
"""

import json
from pprint import pprint

users_data = 'data/users.csv'
hobbys_data = 'data/hobbys.csv'
out_data = 'data/outdata.txt'
user_dict = {}

with open(users_data, 'r', encoding='utf-8') as users, \
     open(hobbys_data, 'r', encoding='utf-8') as hobbys, \
     open(out_data, 'a', encoding='utf-8') as out_data:
    while True:
        user_line = users.readline().strip()
        if user_line:
            while True:
                hobby_line = hobbys.readline().strip()
                if not hobby_line:
                    user_dict[user_line.replace(',', ' ')] = 'None'
                else:
                    user_dict[user_line.replace(',', ' ')] = hobby_line.replace(',', ', ')
                break
        elif hobby_line != '':
            exit(1)
        else:
            break
    print(json.dumps(user_dict), file=out_data)

pprint(user_dict, width=60)
print(type(user_dict))
