"""
2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего
задания. Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
размер которых превышает объем ОЗУ компьютера.
"""


tmp_dict = {}

with open('nginx_logs.txt', 'r') as res_file:
    for line in res_file:

        if not line:
            break

        remote_addr = line[0:line.find(' ')]
        request_type = line[line.find('"')+1:line.find(' ', line.index('"'))]
        requested_resource = line[line.find('/', line.index('"')):line.find('HTTP')-1]

        tmp_dict.setdefault(remote_addr, 0)
        tmp_dict[remote_addr] += 1

spammer = {}
mes_max = 0

for k, v in tmp_dict.items():
    if v > mes_max:
        mes_max = v
        spammer = [k, v]

print('spammer is ', spammer)
