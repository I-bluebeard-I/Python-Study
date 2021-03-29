"""
7. * (вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта: передаём ему номер записи
и новое значение. При этом файл не должен читаться целиком — обязательное требование. Предусмотреть ситуацию, когда
пользователь вводит номер записи, которой не существует.
"""


# python part01_lesson06_task07.py Edit_sales 3 174i57384,45


import sys
from os import replace

if sys.argv[1].lower() != 'add_sale' and\
   sys.argv[1].lower() != 'show_sales' and \
   sys.argv[1].lower() != 'edit_sales' or\
   sys.argv[1].lower() == 'add_sale' and len(sys.argv) != 3 or\
   sys.argv[1].lower() == 'show_sales' and len(sys.argv) > 4 or \
   sys.argv[1].lower() == 'edit_sales' and len(sys.argv) != 4:
    print('\nДля работы программы введите:\n'
          'PYTHON <имя скрипта.PY> ADD_SALE | SHOW_SALES | EDIT_SALES [параметр_1] [параметр_2]\n\n'
          'ADD_SALE [параметр_1]                      сохраняет данные о продажах\n'
          'SHOW_SALES                                 выводить все записи о продажах\n'
          'SHOW_SALES [параметр_1]                    выводит данные о продажах начиная с указанной позиции\n'
          'SHOW_SALES [параметр_1] [параметр_2]       выводит данные о продажах в заданнром диапазоне\n'
          'EDIT_SALES [номер_строки] [новое_значение] заменят данные о продажах в указанной строке')
    exit(0)


source_file = "data/bakery.csv"
tmp_source = "data/bakery.bak"

if sys.argv[1].lower() == 'edit_sales':
    with open(source_file, 'a+', encoding='UTF-8') as source, \
         open(tmp_source, 'w', encoding='UTF-8') as tmp:
        source.seek(0)
        count = 1
        while True:
            line = source.readline().strip()
            if not line:
                break
            if count == int(sys.argv[2]):
                print(sys.argv[3], file=tmp)
            else:
                print(line, file=tmp)
            count += 1

    replace(tmp_source, source_file)

    if int(sys.argv[2]) > count:
        print('Записи с таким номером не существует. Введите значение от 1 до', count)

elif sys.argv[1].lower() == 'add_sale':
    with open(source_file, 'a+', encoding='UTF-8') as source:
        print(sys.argv[2], file=source)

elif sys.argv[1].lower() == 'show_sales':
    with open(source_file, 'a+', encoding='UTF-8') as source:
        if len(sys.argv) == 2: # просто запуск скрипта — выводить все записи;
            source.seek(0)
            while True:
                line = source.readline().strip()
                print(line)
                if not line:
                    break

        elif len(sys.argv) == 3: # запуск скрипта с одним параметром-числом —
                                 # выводить все записи с номера, равного этому числу, до конца;
            source.seek(0)
            count = 1
            while True:
                line = source.readline().strip()
                if count >= int(sys.argv[2]):
                    print(line)
                count += 1
                if not line:
                    break

        elif len(sys.argv) == 4: # запуск скрипта с двумя числами — выводить записи, начиная с номера,
                                 # равного первому числу, по номер, равный второму числу, включительно.
            source.seek(0)
            count = 1
            while True:
                line = source.readline().strip()
                if int(sys.argv[2]) <= count <= int(sys.argv[3]):
                    print(line)
                count += 1
                if not line:
                    break
