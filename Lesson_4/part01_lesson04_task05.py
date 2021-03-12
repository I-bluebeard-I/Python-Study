"""
Задание 5. * Вызов с командной строки
Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли,
а коды валют ему дожны передавать через аргументы командной строки (там может быть один или несколько кодов).
Вывод курсов сделать в том же порядке, что присланные аргументы
Например:

python task5.py USD EUR
USD 75.18, 2020-09-05
EUR 80.35, 2020-09-05
"""

# python part01_lesson04_task05.py usd eur gbp aud byr jpy brl hkd dkk

import sys

from utils import get_currency_rate


for param in range(len(sys.argv)-1):

    currency_char_code = sys.argv[param+1]
    print(f'{currency_char_code.upper()} '
          f'{get_currency_rate(currency_char_code)[0]}, '
          f'{get_currency_rate(currency_char_code)[1]}')
