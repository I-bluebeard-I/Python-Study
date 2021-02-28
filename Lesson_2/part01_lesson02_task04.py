"""
4. Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'
Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду. Можно ли при этом не
создавать новый список?
"""

workers = [
    'инженер-конструктор Игорь',
    'главный бухгалтер МАРИНА',
    'токарь высшего разряда нИКОЛАй',
    'директор аэлита'
]

for worker in workers:
    worker_name = worker.split()[-1]
    print(f'Привет, {worker_name.capitalize()}!')

