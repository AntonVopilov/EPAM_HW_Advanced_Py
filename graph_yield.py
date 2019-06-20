""""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной
Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)
"""


class Graph:
    """
    Возвращает генератор вершин графа при обходе в ширину
    """

    def __init__(self, E: dict):
        if isinstance(E, dict):
            self.E = E
        else:
            raise TypeError('You send {0} object'.format(E.__class__))

        if len(self.E) == 0:
            raise TypeError('You graph is empty')

        for key, values in self.E.items():
            for val in values:
                if val not in self.E:
                    raise TypeError('You graph does not contain description of this vernice', val)

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


if __name__ == '__main__':

    E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}

    graph = Graph(E)

    for i in graph:
        print(i)
