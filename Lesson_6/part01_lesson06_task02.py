"""
2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего
задания. Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
размер которых превышает объем ОЗУ компьютера.
"""


import json

with open('nginx_logs.txt', 'r') as res_file:
    while True:

        with open('nginx_logs_parsed.txt', 'a') as parsed_file:
            for line in res_file:

                if not line:
                    break

                remote_addr = line[0:line.find(' ')]
                request_type = line[line.find('"')+1:line.find(' ', line.index('"'))]
                requested_resource = line[line.find('/', line.index('"')):line.find('HTTP')-1]

                tmp_tuple = remote_addr, request_type, requested_resource
                print(json.dumps(tmp_tuple), file=parsed_file)
