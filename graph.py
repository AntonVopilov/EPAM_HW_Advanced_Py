""""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной
Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)
"""


class Graph:
    def __init__(self, E: dict):
        self.E = E

        self._visited_status = {key: False for key in self.E.keys()}
        self._iter_dict = iter(self.E.items())
        self._key, self._value = next(self._iter_dict)
        self._iter_value = iter(self._value)

    def __iter__(self):
        return self

    def __next__(self):

        if not self._visited_status[self._key]:
            self._visited_status[self._key] = True
            return self._key

        try:
            ver = next(self._iter_value)

        except StopIteration:

            try:
                self._key, self._value = next(self._iter_dict)
                self._iter_value = iter(self._value)
                return self.__next__()

            except StopIteration:
                self._iter_dict = iter(self.E)
                raise StopIteration

        if not self._visited_status[ver]:
            self._visited_status[ver] = True
            return ver
        else:
            return self.__next__()



E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
F = {'A': ['B', 'C', 'D'], 'B': ['M', 'N'], 'C': ['Y'], 'D': ['F', 'G'], 'F': [], 'G': [], 'N': [], 'Y': [], 'M': []}
graph = Graph(F)


for vertice in graph:
    print(vertice)
