import polska

class Vertex:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return str(self.key)

class ListGraph:
    def __init__(self):
        self.list = {}

    def is_empty(self):
        return len(self.list) == 0

    def insert_vertex(self, vertex):
        self.list[vertex] = {}

    def insert_edge(self, vertex1, vertex2, edge=None):
        self.list.setdefault(vertex1, {})[vertex2] = edge

        self.list.setdefault(vertex2, {})[vertex1] = edge

    def delete_vertex(self, vertex):
        if vertex in self.list:
            self.list.pop(vertex)
            for i in self.vertices():
                self.list[i].pop(vertex, None)

    def delete_edge(self, vertex1, vertex2):
        if vertex1 in self.list and vertex2 in self.list[vertex1]:
            self.list[vertex1].pop(vertex2)

        if vertex2 in self.list and vertex1 in self.list[vertex2]:
            self.list[vertex2].pop(vertex1)

    def neighbours(self, vertex_id):
        return self.list[vertex_id].items()

    def vertices(self):
        return self.list.keys()

    def get_vertex(self, vertex_id):
        return vertex_id

class MatrixGraph:
    def __init__(self, def_val=0):
        self.def_val = def_val
        self.list = []
        self.val = []

    def is_empty(self):
        return len(self.list) == 0

    def insert_vertex(self, vertex):
        for i in self.list:
            i.append(self.def_val)

        self.list.append([self.def_val for _ in range(len(self.list) + 1)])
        self.val.append(vertex)

    def insert_edge(self, vertex1, vertex2, edge=1):
        id_1 = self.get_vertex_id(vertex1)
        id_2 = self.get_vertex_id(vertex2)

        if id_1 == None:
            self.insert_vertex(vertex1)
            id_1 = len(self.val) - 1

        if id_2 == None:
            self.insert_vertex(vertex2)
            id_2 = len(self.val) - 1
            
        self.list[id_1][id_2] = edge
        self.list[id_2][id_1] = edge

    def delete_vertex(self, vertex):
        id = self.get_vertex_id(vertex)

        if id != None:
            self.list.pop(id)
            for i in self.vertices():
                self.list[i].pop(id)
            self.val.pop(id)

    def delete_edge(self, vertex1, vertex2):
        id_1 = self.get_vertex_id(vertex1)
        id_2 = self.get_vertex_id(vertex2)
        if id_1 != None and id_2 != None:
            self.list[id_1][id_2] = self.def_val
            self.list[id_2][id_1] = self.def_val

    def neighbours(self, vertex_id):
        res = []
        for i in range(len(self.val)):
            if self.list[vertex_id][i] != self.def_val:
                res.append((i, self.list[vertex_id][i]))
        return res

    def vertices(self):
        return [i for i in range(len(self.val) - 1)]

    def get_vertex_id(self, index):
        id = 0
        for i in self.val:
            if i == index:
                return id
            id += 1
        return None
    
    def get_vertex(self, vertex_id):
        return self.val[vertex_id]
    
def test(graf):
    [graf.insert_edge(Vertex(edge[0]), Vertex(edge[1])) for edge in polska.graf]

    graf.delete_edge(Vertex('W'), Vertex('E'))
    graf.delete_vertex(Vertex('K'))
    polska.draw_map(graf)

def main():
    macierz = MatrixGraph()
    lista = ListGraph()
    test(macierz)
    test(lista)

if __name__ == "__main__":
    main()