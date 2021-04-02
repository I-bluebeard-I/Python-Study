"""
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех слов, взятых из трёх списков
(по одному слову из каждого списка):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        Например:
#>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое
слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""


def get_jokes(num_of_joke, **kwargs):
    '''
    Функция возвращает n-шуток, сформированных из трех слов, взятых из трёх списков
    (по одному слову из каждого списка): nouns, adverbs, adjectives.

    Если флаг 'flag' = 1, повторы шуток, в пределах длинн списков, запрещены.
        Функция создает копии исходных списков, после использования слово удаляется из копии списка.
        При n-шуток > длинн списков, копии списков воосстанавливаются до исходного значения.

    Если флаг 'flag' <> 1, повторное использование слов в шутках не контроллируется.

    '''

    from random import randint
    from copy import copy

    tmp_nouns = copy(kwargs['nouns'])
    tmp_adverbs = copy(kwargs['adverbs'])
    tmp_adjectives = copy(kwargs['adjectives'])

    for i in range(num_of_joke):
        joke.append(f'{tmp_nouns[randint(0, len(tmp_nouns)-1)]} '
                    f'{tmp_adverbs[randint(0, len(tmp_adverbs)-1)]} '
                    f'{tmp_adjectives[randint(0, len(tmp_adjectives)-1)]}')

        if flag == 1:
            rem_nouns, rem_adverbs, rem_adjectives = joke[-1].split()
            tmp_nouns.remove(rem_nouns)
            tmp_adverbs.remove(rem_adverbs)
            tmp_adjectives.remove(rem_adjectives)

            if len(tmp_nouns) == 0 or len(tmp_adverbs) == 0 or len(tmp_adjectives) == 0:
                # Оригинальные шутки закончились, дальше буду повторяться...
                tmp_nouns = copy(kwargs['nouns'])
                tmp_adverbs = copy(kwargs['adverbs'])
                tmp_adjectives = copy(kwargs['adjectives'])

    return joke


flag = 1                                                               # флаг уникальных шуток, 1 = повторы запрещены

help(get_jokes)
num_of_joke = int(input('Сколько раз шутим? >>> '))

joke = []
get_jokes(num_of_joke,
          nouns=["автомобиль", "лес", "огонь", "город", "дом"],
          adverbs=["сегодня", "вчера", "завтра", "позавчера", "ночью"],
          adjectives=["веселый", "яркий", "зеленый", "утопичный", "мягкий"])
print(*joke, sep=', ')
