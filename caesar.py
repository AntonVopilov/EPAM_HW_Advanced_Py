"""
Реализовать дескриптор, кодирующий слова с помощью шифра Цезаря
"""

import string

letters = string.ascii_lowercase


def caesar(message: str, shift):
    res = ''
    len_letters = len(letters)
    for char in message:
        index_count = lambda index_shift: index_shift if index_shift <= len_letters else \
            index_count(index_shift % len_letters)
        res += letters[index_count(letters.index(char) + shift)]
    return res


class ShiftDescriptor:
    def __init__(self, shift):
        self.shift = shift

    def __get__(self, obj, type_self=None):
        return caesar(obj.__dict__[self.shift], self.shift)

    def __set__(self, obj, value) -> None:
        obj.__dict__[self.shift] = value


class CeasarSipher:
    message = ShiftDescriptor(4)
    another_message = ShiftDescriptor(7)


a = CeasarSipher()

a.message = 'abc'
a.another_message = 'hello'


assert a.message == 'efg'
assert a.another_message == 'olssv'