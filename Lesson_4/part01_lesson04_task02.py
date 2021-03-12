"""
Задание 2. Курс Валюты
Написать функцию get_currency_rate(), принимающую в качестве аргумента код валюты
(например, USD, EUR, GBP, ...) в виде строки и возвращающую курс этой валюты по отношению к рублю.
Код валюты может быть в произвольном регистре.
Функция должна возвращать результат числового типа, например float.
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Используйте библиотеку requests, чтобы забрать актуальные данные из ЦБ РФ по адресу
http://www.cbr.ru/scripts/XML_daily.asp.

Выведите на экран курсы для доллара и евро, используя написанную функцию.

Рекомендация: выполнить предварительно запрос к этой странице в обычном браузере, посмотреть содержимое ответа.
"""


def get_currency_rate(currency_char_code):

    import requests

    try:
        page = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

        string_char_code = f'<CharCode>{currency_char_code.upper()}</CharCode>'
        string_value_start = '<Value>'
        string_value_end = '</Value>'

        currency_char_code_position = page.text.find(string_char_code)
        start_index = page.text.find(string_value_start, currency_char_code_position) + len(string_value_start)
        stop_index = page.text.find(string_value_end, currency_char_code_position)

        global currency_value
        currency_value = page.text[start_index:stop_index]
        currency_value = float('.'.join(currency_value. split(',')))

    except:
        currency_value = None

    return currency_value


currency_value = None

currency_char_code = input('Введите код валюты (например, USD, EUR, GBP, ...): ')
try:
    print(f'{currency_char_code.upper()} {get_currency_rate(currency_char_code):4.2f}', type(currency_value))
except:
    print(get_currency_rate(currency_char_code), type(currency_value))
