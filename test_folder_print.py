import os
import tempfile

import pytest
from folder_print import PrintableFolder, folder_to_str


@pytest.mark.parametrize('nonfolders', [
    '', 'abc', [], set(), {}
])
def test_nonfolder(nonfolders):
    with pytest.raises(TypeError):
        folder_to_str(nonfolders)


with tempfile.TemporaryDirectory() as directory:
    def test_make_object(path=tempfile.gettempdir()):
        assert PrintableFolder(path)


def test_print_example():
    paths = ['/folder1', '/folder1/folder1_1', '/folder1/folder1_2', '/folder1/folder1_2/folder1_2_1']
    expected = "V folder1\n|->V folder1_1\n|->V folder1_2\n|  |->V folder1_2_1"
    cwd = os.getcwd()

    for path in paths:
        os.mkdir(os.path.join(cwd + path))

    res = PrintableFolder(cwd + '/folder1').__str__()
    assert all([char[0] == char[1] for i, char in enumerate(zip(res, expected))])

    for path in paths[::-1]:
        os.rmdir(os.path.join(cwd + path))
