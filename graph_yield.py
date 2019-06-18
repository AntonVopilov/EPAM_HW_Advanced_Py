""""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной
Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)
"""


class Graph:
    def __init__(self, E: dict):
        self.E = E
        self._visited_status = set()

    def __iter__(self):

        for key, values in self.E.items():
            if key not in self._visited_status:
                self._visited_status.add(key)
                yield key

            for val in values:
                if val not in self._visited_status:
                    self._visited_status.add(val)
                    yield val

    def __next__(self):
        return next(self.__iter__())





E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
F = {'A': ['B', 'C', 'D'], 'B': ['M', 'N'], 'C': ['Y'], 'D': ['F', 'G'], 'F': [], 'G': [], 'N': [], 'Y': [], 'M': []}

graph = Graph(F)


for i, vertice in enumerate(graph):
    print(i, vertice)
