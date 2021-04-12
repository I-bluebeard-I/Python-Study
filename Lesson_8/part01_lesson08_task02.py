"""
2. * (вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) для получения информации
вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>),
например:

raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian
APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки? Можно
ли для них уточнить регулярное выражение?
"""


import re

with open('../lesson_6/nginx_logs.txt', 'r') as res_file, \
       open('nginx_logs_parsed2.txt', 'a') as parsed_file:
       for line in res_file:

              parsed_line = []
              parsed_line.append(re.compile(r'(?:\d{,3}[.]){3}\d+(?=\s)|(?:\w+[:]){7}\w+(?=\s)').findall(line)) # <remote_adr>
              parsed_line.append(re.compile(r'(?<=\[)\d.*(?=\])').findall(line))                                # <request_datetime>
              parsed_line.append(re.compile(r'(?<=\")\w+(?=\s\/)').findall(line))                               # <request_type>
              parsed_line.append(re.compile(r'(?:\/\w+){1,}(?=\s)').findall(line))                              # <requested_resource>
              parsed_line.append(re.compile(r'(?<=\s)\d..(?=\s\d+)').findall(line))                             # <response_code>
              parsed_line.append(re.compile(r'(?<=\s)\d+(?=\s"-")').findall(line))                              # <response_size>

              print(*parsed_line, file=parsed_file)
print('nginx_logs_parsed2.txt writed')
