graf = [ ('A','B',4), ('A','C',1), ('A','D',4),
         ('B','E',9), ('B','F',9), ('B','G',7), ('B','C',5),
         ('C','G',9), ('C','D',3),
         ('D', 'G', 10), ('D', 'J', 18),
         ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
         ('F', 'H', 2), ('F', 'G', 8),
         ('G', 'H', 9), ('G', 'J', 8),
         ('H', 'I', 3), ('H','J',9),
         ('I', 'J', 9)
        ]

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
    
    def size(self):
        return len(self.list)
    
class UnionFind:
  def __init__(self, n):
    self.p = [x for x in range(n)]
    self.size = [1 for _ in range(n)]
    self.n = n
  
  def find(self, v ):
    if self.p[v] == v:
      return v
    
    self.p[v] = self.find(self.p[v])
    return self.p[v]
  
  def union_sets(self, u, v):
    uRoot = self.find(u)
    vRoot = self.find(v)
    if self.size[uRoot] > self.size[vRoot]:
      self.p[vRoot] = uRoot
    elif self.size[uRoot] < self.size[vRoot]:
      self.p[uRoot] = vRoot
    elif uRoot != vRoot:
      self.p[uRoot] = vRoot
      self.size[vRoot] += 1

  def same_components(self, s1, s2):
    return self.find(s1) == self.find(s2)
  
def convertToNumber(sign):
  return ord(sign) - 65


def test1():
  n = 6
  edges = [(1,2),(1,4), (1,5), (4,5)]
  check = [(1,2),(2,3),(4,5), (1,4)]
  vertices = []
  uf = UnionFind(n)
  for i in range(n):
    vertices.append(n)
    
  
  for v1, v2 in edges:
    uf.union_sets(v1, v2)
  for v1, v2 in check:
    print(uf.same_components(v1,v2))
    

vertex_indices = {vertex_label: index for index, vertex_label in enumerate(set(v1 for v1, _, _ in graf))}

def kruskal(edges):
    edges = sorted(edges, key=lambda edge: (edge[2], edge[0], edge[1]))
    g = Graph()

    for n1, n2, e in edges:
        g.insert_edge(n1, n2, e)

    uf = UnionFind(len(vertex_indices))
    for v1, v2, _ in edges:
        v1_index = vertex_indices[v1]
        v2_index = vertex_indices[v2]
        if uf.same_components(v1_index, v2_index):
            g.delete_edge(v1, v2)
        else:
            uf.union_sets(v1_index, v2_index)
    return gg
  
  
def main():
  g = kruskal(graf)
  g.printGraph()
  
if __name__ == '__main__':
  main()
    