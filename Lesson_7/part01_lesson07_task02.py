"""
2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками»
(не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
"""


def create_structure():

    import os

    outdata_dir = 'data/2/'
    config_file = 'data/config2.yaml'
    level = {}
    parent = []

    with open(config_file, 'r', encoding='utf-8') as config:
        string_count = 1
        while True:
            line = config.readline()
            if not line:
                break

            level[string_count] = (round(line.count(' ') / 3), line.strip().replace('--', '').replace('|', '').strip())

            if string_count > 1:
                if level[string_count][0] > level[string_count - 1][0]:
                    parent.append(level[string_count - 1][1])
                elif level[string_count][0] < level[string_count - 1][0]:
                    a = level[string_count - 1][0] - level[string_count][0]
                    for i in range(a):
                        parent.pop()

            file_path = os.path.join(outdata_dir, *parent, level[string_count][1]).replace('\\', '/')

            if level[string_count][1].find('.') != -1:
                with open(file_path, 'a', encoding='utf-8'):
                    pass
            else:
                try:
                    os.makedirs(file_path)
                except FileExistsError:
                    pass

            string_count += 1


create_structure()
