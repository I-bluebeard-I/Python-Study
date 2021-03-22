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

import os
from pprint import pprint


users_data = 'data/users.csv'
hobbys_data = 'data/hobbys.csv'
hobby = []
user_dict = {}

with open(users_data, 'r', encoding='utf-8') as users, \
     open(hobbys_data, 'r', encoding='utf-8') as hobbys:
    for hobby_line in hobbys:
        hobby.append(hobby_line.strip())

    n=0
    for user_line in users:
        if not user_line:
            exit(1)

        if n < len(hobby):
            user_dict[user_line.strip()] = hobby[n]
        elif n >= len(hobby):
            user_dict[user_line.strip()] = 'None'
        n += 1

pprint(user_dict, width=40)
print(type(user_dict))
