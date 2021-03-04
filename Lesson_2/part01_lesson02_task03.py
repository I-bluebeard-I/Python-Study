"""
3. * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place). Эта задача намного серьёзнее,
чем может сначала показаться.
Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел
со знаком?

Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
Новый список не создавать! Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
"""


original_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

print(id(original_list), '- ID оригинального списка')

for word in range(len(original_list)):

    if original_list[word].isdigit():
        if len(original_list[word]) < 2:
            original_list[word] = f'"0{original_list[word]}"'
        else:
            original_list[word] = f'"{original_list[word]}"'

    for symbol in original_list[word]:
        if symbol in '+-':
            if len(original_list[word]) > 2:
                original_list[word] = f'"{original_list[word]}"'
            else:
                original_list[word] = f'"{original_list[word][:1]}0{original_list[word][1:]}"'

print(' '.join(original_list))
print(type(' '.join(original_list)))
print(id(original_list), '- ID обработанного списка')
