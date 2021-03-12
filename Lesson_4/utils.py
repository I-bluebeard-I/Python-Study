def get_currency_rate(currency_char_code):

    import requests
    import datetime
    from decimal import Decimal, ROUND_HALF_EVEN

    try:
        page = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

        #global date_value

        string_date = 'ValCurs Date="'
        value_start = page.text.find(string_date) + len(string_date)
        value_end = value_start + 10   # dd.mm.yyyy

        date_value = page.text[value_start: value_end]
        date_value = datetime.date(int(date_value[-4:]), int(date_value[3:5]), int(date_value[0:2]))

        #global currency_value

        string_char_code = f'<CharCode>{currency_char_code.upper()}</CharCode>'
        currency_value_start = '<Value>'
        currency_value_end = '</Value>'

        currency_char_code_position = page.text.find(string_char_code)
        start_index = page.text.find(currency_value_start, currency_char_code_position) + len(currency_value_start)
        stop_index = page.text.find(currency_value_end, currency_char_code_position)
        currency_value = page.text[start_index:stop_index]
        currency_value = Decimal('.'.join(currency_value. split(','))).quantize(Decimal('.00'), rounding=ROUND_HALF_EVEN)

    except:
        currency_value = None

    return currency_value, date_value