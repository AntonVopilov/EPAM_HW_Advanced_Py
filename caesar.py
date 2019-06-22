"""
Реализовать дескриптор, кодирующий слова с помощью шифра Цезаря
"""

import string

letters = string.ascii_lowercase


def caesar(message: str, shift):

    if not isinstance(message, str):
        raise TypeError('messege is not string')

    if not isinstance(shift, int):
        raise TypeError('shift is not int')

    res = ''

    len_letters = len(letters)
    if len_letters == 0:
        return res
    for char in message:
        index_count = lambda index_shift: index_shift if index_shift < len_letters else \
            index_count(index_shift % len_letters)
        try:
            res += letters[index_count(letters.index(char) + shift)]
        except ValueError:
            res += char
    return res


class ShiftDescriptor:
    def __init__(self, shift):
        self.shift = shift
        self._id_name = id(self)


    def __get__(self, obj, type_self=None):
        return caesar(obj.__dict__[self._id_name], self.shift)

    def __set__(self, obj, value) -> None:
        obj.__dict__[self._id_name] = value


class CeasarSipher:
    message = ShiftDescriptor(4)
    another_message = ShiftDescriptor(7)


if __name__ == '__main__':


    a = CeasarSipher()
    a.message = 'abc'
    a.another_message = 'hello'

    print(a.another_message)

    assert a.message == 'efg'
    assert a.another_message == 'olssv'