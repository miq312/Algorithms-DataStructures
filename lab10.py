import graf_mst

class Vertex:
    def __init__(self, key):
        self.key = key

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return isinstance(other, Vertex) and self.key == other.key

    def __str__(self):
        return str(self.key)

class Edge:
    def __init__(self, capacity, is_residual = False):
        self.capacity = capacity
        self.is_residual = is_residual
        if not is_residual:
            self.flow = 0
            self.residual = capacity
        else:
            self.flow = capacity
            self.residual = 0

    def __repr__(self):
        return f"{self.capacity} {self.flow} {self.residual} {self.is_residual}"
    
class Graph:
    def __init__(self):
        self.list = {}

    def is_empty(self):
        return len(self.list) == 0

    def insert_vertex(self, vertex):
        if vertex in self.list:
            return
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

def prim(graph: Graph):
    mst = Graph()

    intree = dict.fromkeys(graph.vertices(), 0)
    distance = dict.fromkeys(graph.vertices(), float('inf'))
    parent = dict.fromkeys(graph.vertices(), None)
    vertices_iter = iter(graph.vertices())
    v = next(vertices_iter)
    total_weight = 0

    while not intree[v]:
        intree[v] = 1

        for i, j in graph.neighbours(v):
            if not intree[i] and j < distance[i]:
                distance[i] = j
                parent[i] = v

        candidates = {vertex: dist for vertex, dist in distance.items() if not intree[vertex]}
        if candidates:
            v = min(candidates, key = candidates.get)
            if parent[v] is not None:
                mst.insert_edge(v, parent[v], distance[v])
                total_weight += distance[v]
        else:
            break

    return mst

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")

def main():
    graf = Graph()

    for edge in graf_mst.graf:
        vertex1, vertex2, weight = edge
        graf.insert_edge(Vertex(vertex1), Vertex(vertex2), weight)

    mst = prim(graf)
    printGraph(mst)

if __name__ == '__main__':
    main()
