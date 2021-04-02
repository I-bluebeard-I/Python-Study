"""
2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с
числительными, начинающимися с заглавной буквы. Например:
# >>> num_translate_adv("One")
"Один"
@ >>> num_translate_adv("two")
"два"
"""


def num_translate_adv(en_number):

    dictionary = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }
    if en_number.istitle():
        return dictionary.get(en_number.lower()).capitalize()
    else:
        return dictionary.get(en_number)


number = input('Введите числительное от 0 до 10 на английском (zero/ one/ two...): ')
print(num_translate_adv(number))
