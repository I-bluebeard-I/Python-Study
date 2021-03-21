"""
1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список
кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
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
