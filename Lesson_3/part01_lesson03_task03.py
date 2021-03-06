"""
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в котором
ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Сможете ли вы вернуть отсортированный по ключам словарь?
"""

from pprint import pprint


def thesaurus(*args):
    list_of_args = [*args]

    for i in range(len(list_of_args)):
        key = list_of_args[i][0]
        value = list_of_args[i]

        if key not in dictionary:
            dictionary[key] = [value]
        else:
            dictionary[key].append(value)

    sorted(dictionary.keys())

    return dictionary


dictionary = {}

thesaurus('Харитон', 'Иван', 'Мария', 'Петр', 'Илья', 'Анна', 'Максим')
pprint(dictionary)
