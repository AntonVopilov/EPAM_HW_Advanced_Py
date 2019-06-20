import pytest
from folder_print import PrintableFolder, folder_to_str

#folder = '/Users/antonvopilov/Desktop'
#print(PrintableFolder(folder))

@pytest.mark.parametrize('nonfolders', [
    '', 'abc', [], set(), {}
])
def test_nonfolder(nonfolders):
    with pytest.raises(TypeError):
        folder_to_str(nonfolders)

import os
import  tempfile
import  time



with tempfile.TemporaryDirectory() as directory:

    print('generate path', PrintableFolder(tempfile.gettempdir()))
    print(os.getcwd())
    time.sleep(30)
# @pytest.mark.parametrize('data', [
#     set(), list()
# ])
# def test_type_of_graph_instance(data):
#     with pytest.raises(TypeError):
#         Graph(data)
#
#
# @pytest.mark.parametrize('data', [
#     {}, {'A': ['B', 'C', 'D']}
# ])
# def test_type_of_graph_instance(data):
#     with pytest.raises(TypeError):
#         Graph(data)
#
#
# @pytest.mark.parametrize('data', [
#     {'A': ['B', 'C', 'D'], 'B': ['M', 'N'], 'C': ['Y'], 'D': ['F', 'G'], 'F': [], 'G': [], 'N': [], 'Y': [],
#      'M': []},
#     {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
#
# ])
# def test_order_of_printing(data):
#     graph = Graph(data)
#
#     previous_vers = data[next(graph)]
#     for ver in graph:
#
#         if not previous_vers:
#             previous_vers = data[ver]
#         elif ver != previous_vers[-1]:
#             assert ver in previous_vers
#         else:
#             previous_vers = []
#