"""
6. Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта с интерфейсом
командной строки: для записи данных и для вывода на экран записанных данных. При записи передавать из командной
строки значение суммы продаж. Для чтения данных реализовать в командной строке следующую логику:
. просто запуск скрипта — выводить все записи;
. запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
. запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный второму
числу, включительно.
Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. Примеры запуска скриптов:

python add_sale.py 5978,5
python add_sale.py 8914,3
python add_sale.py 7879,1
python add_sale.py 1573,7
python show_sales.py
5978,5
8914,3
7879,1
1573,7
python show_sales.py 3
7879,1
1573,7
python show_sales.py 1 3
5978,5
8914,3
7879,1
"""


# python part01_lesson06_task06.py show_sales 1573,7


import sys

if sys.argv[1].lower() == 'add_sale' and len(sys.argv) > 2 or\
   sys.argv[1].lower() == 'show_sales' and len(sys.argv) > 4:
    print('\nДля работы программы наберите:\n'
          'PYTHON <имя скрипта.PY> ADD_SALE | SHOW_SALES [параметр_1] [параметр_2]\n\n'
          'ADD_SALE [параметр_1]                      сохраняет данные о продажах\n'
          'SHOW_SALES                                 выводить все записи о продажах\n'
          'SHOW_SALES [параметр_1]                    выводит данные о продажах начиная с указанной позиции\n'
          'SHOW_SALES [параметр_1] [параметр_2]       выводит данные о продажах в заданнром диапазоне')
    exit(0)

source_file = "data/bakery.csv"

with open(source_file, 'a+', encoding='UTF-8') as source:

    if sys.argv[1].lower() == 'add_sale':
            print(sys.argv[2], file=source)

    elif sys.argv[1].lower() == 'show_sales':

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
