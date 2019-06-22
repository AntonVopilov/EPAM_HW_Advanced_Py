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
        self._graph_gen = None

    
    def __iter__(self):
        key_end  = len(self.E.keys()) 
        value_end = None

        visited_ver = set()
        for key, values in self.E.items():
            key_end -= 1
            if key not in visited_ver:
                visited_ver.add(key)
                yield key

            if  key_end == 0:
                value_end = True

            for i, val in enumerate(values):
                if val not in visited_ver:
                    visited_ver.add(val)
                    if value_end and i == len(self.E[key]):
                        yield val
                        raise StopIteration
                    else:
                        yield val
       
        
if __name__ == '__main__':

    E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}

    graph = Graph(E)
    for i in graph:
        print(i)
   
    print('\n')
   
    for i in graph:
        for j in graph:
            print(i, j)
    

