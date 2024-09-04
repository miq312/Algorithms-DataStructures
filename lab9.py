class Vertex:
    def __init__(self, key):
        self.key = key

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self.key == other.key

    def __str__(self):
        return str(self.key)

class ListGraph:
    def __init__(self):
        self.list = {}

    def is_empty(self):
        return len(self.list) == 0

    def insert_vertex(self, vertex):
        self.list.setdefault(vertex, {})

    def insert_edge(self, vertex1, vertex2, capacity):
        if vertex1 != vertex2:
            self.insert_vertex(vertex1)
            self.insert_vertex(vertex2)
            
            self.list.setdefault(vertex1, {})[vertex2] = Edge(capacity)
            self.list.setdefault(vertex2, {})[vertex1] = Edge(capacity, is_residual=True)

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
        for vertex in self.vertices():
            if vertex.key == vertex_id:
                return vertex

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

def printGraph(g):
        print("------GRAPH------")
        for v in g.vertices():
            print(v, end = " -> ")
            for (n, w) in g.neighbours(v):
                print(n, w, end=";")
            print()
        print("-------------------")

def BFS(graph, s):
    visited = set()
    parent = {}
    q = []
    
    visited.add(s)
    q.append(s)

    while q:
        current = q.pop(0)

        for n, e in graph.neighbours(current):
            if n not in visited and e.residual > 0:
                visited.add(n)
                parent[n] = current
                q.append(n)

    return parent

def findMin(graph, parent, source, target):
    min_capacity = float('inf')
    current = target

    if target not in parent:
        return 0

    while current != source:
        parent_vertex = parent.get(current)
        if parent_vertex not in graph.list:
            return 0
        edge = graph.list.get(parent_vertex, {}).get(current)
        if edge is None:
            return 0
        min_capacity = min(min_capacity, edge.residual)
        current = parent_vertex 

    return min_capacity

def updateFlow(graph, parent, min_capacity, source, target):
    current = target

    while current != source:
        parent_vertex = parent.get(current)
        if parent_vertex is None or current not in graph.list.get(parent_vertex, {}):
            return False
        
        edge = graph.list[parent_vertex][current]
        flow_change = min_capacity if not edge.is_residual else -min_capacity
        edge.flow += flow_change
        edge.residual -= flow_change
        
        current = parent_vertex
        
    return graph

def fordFulkerson(graph, source='s', target='t'):
    max_flow = 0
    
    while True:
        parent = BFS(graph, source)

        if target not in parent:
            break

        min_capacity = findMin(graph, parent, source, target)
        if min_capacity == 0:
            break

        success = updateFlow(graph, parent, min_capacity, source, target)
        if not success:
            break

        max_flow += min_capacity

    return max_flow
    
def main():
    grafy = [[('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)],
             [('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4)],
             [('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]]

    for idx, graf in enumerate(grafy):
        graph = ListGraph()
        
        for i in graf:
            vertex1 = Vertex(i[0])
            vertex2 = Vertex(i[1])
            graph.insert_edge(vertex1, vertex2, i[2])

        max_flow = fordFulkerson(graph, graph.get_vertex('s'), graph.get_vertex('t'))
        print(f"Maksymalny przepływ dla grafu {idx}: {max_flow}\n")
        printGraph(graph)
        print()


if __name__ == '__main__':
    main()
