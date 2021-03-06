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


def get_jokes(num_of_joke, *args):
    # Документация

    from random import randint
    joke = []

    for i in range(num_of_joke):
        joke.append(f'{nouns[randint(0, len(nouns)-1)]} '
                    f'{adverbs[randint(0, len(adverbs)-1)]} '
                    f'{adjectives[randint(0, len(adjectives)-1)]}')
    return joke


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

help(get_jokes)                                                         # добавить документацию
num_of_joke = int(input('Сколько раз шутим? '))
print(*get_jokes(num_of_joke, nouns, adverbs, adjectives), sep=', ')



"""
def get_jokes(num_of_joke, *args):

    # Документация

    from random import randint
    joke = []

    for i in range(num_of_joke):
        joke.append(f'{nouns[randint(0, len(nouns)-1)]} '
                    f'{adverbs[randint(0, len(adverbs)-1)]} '
                    f'{adjectives[randint(0, len(adjectives)-1)]}')
    return joke


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

help(get_jokes)                                                         # добавить документацию
num_of_joke = int(input('Сколько раз шутим? '))
print(*get_jokes(num_of_joke, nouns, adverbs, adjectives), sep=', ')
"""