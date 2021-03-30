"""
3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). Написать
скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая
решена, например, во фреймворке django.
"""


from part01_lesson07_task02 import create_structure
import os
import shutil

in_data_dir = 'data/2'
out_data_dir = 'data/3/templates'


create_structure()
dir_list = os.walk(in_data_dir)

for line in dir_list:
    if str(line[2]).find('.html') != -1:
        copy_dir = str(line[0]).replace('\\', '/')
        out_data_app = copy_dir[copy_dir.rfind('/') + 1:]

        try:
            shutil.copytree(copy_dir, os.path.join(out_data_dir, out_data_app).replace('\\', '/'))
        except FileExistsError:
            pass
