"""
4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате
«Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные
по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
#>>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}
Сможете ли вы вернуть отсортированный по ключам словарь?
"""

from pprint import pprint


def thesaurus_adv(*args):

    for i in range(len(args)):
        name, surname = args[i].split()
        key_surname = surname[0]
        key_name = name[0]

        if key_surname not in dictionary:
            dictionary.setdefault(key_surname, [])
            dictionary[key_surname] = {}
        dictionary[key_surname].setdefault(key_name, [])
        dictionary[key_surname][key_name].append(args[i])

    sorted(dictionary.keys())
    return dictionary


dictionary = {}

thesaurus_adv('Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева')
pprint(dictionary, width=40)
