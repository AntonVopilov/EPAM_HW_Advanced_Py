import pytest
from caesar import caesar, CeasarSipher
import random


@pytest.mark.parametrize('initial_string, shift, expected', [
    ('test', 0, 'test'),
    ('abc', 4, 'efg'),
    ('hello', 7, 'olssv'),
    ('caesar', 1503, 'xvznvm')
])
def test_final_result(initial_string, shift, expected):
    assert caesar(initial_string, shift) == expected


@pytest.mark.parametrize('another_chars, shift, expected', [
    (' ', random.randint(0, 1024), ' '),
    ('$%^!*()":>~б_', random.randint(0, 1024), '$%^!*()":>~б_')
])
def test_another_chars(another_chars, shift, expected):
    assert caesar(another_chars, shift) == expected


def test_message_set_get():
    mss_txt = 'message_text'
    obj = CeasarSipher()
    obj.message = mss_txt
    assert obj.__dict__[4] == mss_txt
    assert obj.message == caesar(mss_txt, 4)


def test_another_message_set():
    mss_txt = 'another_message_text'
    obj = CeasarSipher()
    obj.another_message = mss_txt
    assert obj.__dict__[7] == mss_txt
    assert obj.another_message == caesar(mss_txt, 7)
