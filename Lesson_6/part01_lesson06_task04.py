"""
4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ (разумеется, не нужно
реально создавать такие большие файлы, это просто задел на будущее проекта). Также реализовать парсинг данных из
файлов - получить отдельно фамилию, имя и отчество для пользователей и название каждого хобби: преобразовать в
какой-нибудь контейнерный тип (список, кортеж, множество, словарь). Обосновать выбор типа. Подумать, какие могут
возникнуть проблемы при парсинге. В словаре должны храниться данные, полученные в результате парсинга.
"""


users_data = 'data/users.csv'
hobbys_data = 'data/hobbys.csv'
out_data = 'data/outdata.csv'
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
