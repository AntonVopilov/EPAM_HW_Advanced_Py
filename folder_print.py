"""
Реализовать метод __str__, позволяющий выводить все папки и файлы из данной, например так:
> print(folder1)
V folder1
|-> V folder2
|   |-> V folder3
|   |   |-> file3
|   |-> file2
|-> file1
А так же возможность проверить, находится ли файл или папка в другой папке:
> print(file3 in folder2)
True
"""

import os


def folder_to_str(folder):
    folder_marker = 'V '
    inside_marker = '|->'
    space = '|  '

    if not os.path.isdir(folder):
        raise TypeError('You try print non correct path: {0}.'.format(folder))

    if os.path.isfile(folder):
        return os.path.split(folder)[1]

    res = folder_marker + os.path.split(folder)[1] + '\n'

    def walking(folder, depth=0):
        nonlocal res

        obj_in_folder = os.listdir(folder)

        if not obj_in_folder:
            return res

        for enters in os.listdir(folder):
            path = os.path.join(folder, enters)
            if os.path.isdir(path):
                res += depth * space + inside_marker + folder_marker + enters + '\n'
                walking(path, depth + 1)
            if os.path.isfile(path):
                res += depth * space + inside_marker + enters + '\n'
        return res

    return walking(folder)


class PrintableFolder:
    def __init__(self, way):
        self.way = way

    def __str__(self):
        return folder_to_str(self.way)

    def __contains__(self, item):
        return item.way.startswith(self.way)



