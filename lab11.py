class Vertex:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return str(self.key)
    
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
    
class Matrix:
    def __init__(self, matrix, value=0):
        if isinstance(matrix, tuple):
                rows, cols = matrix
                if isinstance(value, int):
                    self.matrix = [[value for _ in range(cols)] for _ in range(rows)]
                else:
                    raise ValueError("Default value must be integer")
        else:
            self.matrix = matrix

    def __add__(self, other):
        if self.size() != other.size():
            raise Exception("Add::Wrong matrix shape")
        else:
            matrix_add = [[0 for _ in range(self.size()[1])] for _ in range(self.size()[0])]
            for i in range(self.size()[0]):
                for j in range(self.size()[1]):
                    matrix_add[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return Matrix(matrix_add)
        
    def __mul__(self, other):
        if self.size()[1] == other.size()[0]:
            matrix_mul = [[0] * other.size()[1] for _ in range(self.size()[0])]

            for i in range(self.size()[0]):
                for j in range(other.size()[1]):
                    for k in range(self.size()[1]):
                        matrix_mul[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return Matrix(matrix_mul)
        else:
            raise Exception("Mul::Wrong matrix shape")
                
    def __getitem__(self, index):
        return self.matrix[index]

    def __str__(self):
        matrix_str = ""
        for row in self.matrix:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str
    
    def size(self):
        return len(self.matrix), len(self.matrix[0])
    
    def __eq__(self, other):
        return self.matrix == other.matrix

    def deepcopy(self):
        return Matrix([row[:] for row in self.matrix])
    
    def transpose(self):
        rows, columns = self.size()
        result = []
        for _ in range(columns):
            row = [0] * rows
            result.append(row)

        for i in range(rows):
            for j in range(columns):
                result[j][i] = self.matrix[i][j]
        return Matrix(result)

def create_M0(P, G):
    rows = len(P.val)
    columns = len(G.val)
    M0 = Matrix((rows, columns), 0)
    for i in range(rows):
        for j in range(columns):
            if len(P.neighbours(i)) <= len(G.neighbours(j)):
                M0.matrix[i][j] = 1
    return M0

def ullmann_v1(using, current_row, matrix_M, P, G, correct_isomorphism, iter):
    iter[0] += 1
    if current_row == len(matrix_M.matrix):
        if check_isomorphism(matrix_M, P, G):
            correct_isomorphism.append(matrix_M.deepcopy())
        return
    for c in range(len(matrix_M.matrix[0])):
        if not using[c]:
            using[c] = True
            matrix_M.matrix[current_row] = [0] * len(matrix_M.matrix[current_row])
            matrix_M.matrix[current_row][c] = 1
            ullmann_v1(using, current_row + 1, matrix_M, P, G, correct_isomorphism, iter)
            using[c] = False

def ullmann_v2(using, current_row, matrix_M, P, G, correct_isomorphism, iter):
    iter[0] += 1
    if current_row == len(matrix_M.matrix):
        if check_isomorphism(matrix_M, P, G):
            correct_isomorphism.append(matrix_M.deepcopy())
        return
    Mc = matrix_M.deepcopy()
    for c in range(len(matrix_M.matrix[0])):
        if not using[c] and matrix_M.matrix[current_row][c] != 0:
            using[c] = True
            Mc.matrix[current_row] = [0] * len(matrix_M.matrix[current_row])
            Mc.matrix[current_row][c] = 1
            ullmann_v2(using, current_row + 1, Mc, P, G, correct_isomorphism, iter)
            using[c] = False

def ullmann_v3(using, current_row, matrix_M, P, G, correct_isomorphism, iter):
    iter[0] += 1
    if current_row == len(matrix_M.matrix):
        if check_isomorphism(matrix_M, P, G):
            correct_isomorphism.append(matrix_M.deepcopy())
        return
    temp = matrix_M.deepcopy()
    prune(temp, P, G)
    for col in range(len(matrix_M.matrix[0])):
        if not using[col] and matrix_M.matrix[current_row][col] != 0:
            using[col] = True
            temp.matrix[current_row] = [0] * len(matrix_M.matrix[current_row])
            temp.matrix[current_row][col] = 1
            ullmann_v3(using, current_row + 1, temp, P, G, correct_isomorphism, iter)
            using[col] = False

def check_isomorphism(M, P, G):
    MT = M.transpose()
    matrixG = Matrix(G.list)
    matrixP = Matrix(P.list)
    res = M * (matrixG * MT)
    return res == matrixP

def prune(M, P, G):
    change = True
    while change:
        change = False
        for i in range(len(M.matrix)):
            for j in range(len(M.matrix[0])):
                if M.matrix[i][j] == 1:
                    neighboursP = P.neighbours(i)
                    neighboursG = G.neighbours(j)
                    if not all(any(M.matrix[x][y] == 1 for y, _ in neighboursG) for x, _ in neighboursP):
                        M.matrix[i][j] = 0
                        change = True

def main():
    graph_G = [('A','B',1),
               ('B','F',1),
               ('B','C',1),
               ('C','D',1),
               ('C','E',1),
               ('D','E',1)]
    
    graph_P = [('A','B',1),
               ('B','C',1),
               ('A','C',1)]
        
    G = MatrixGraph()
    P = MatrixGraph()

    for u, v, w in graph_G:
        G.insert_edge(Vertex(u), Vertex(v), w)

    for u, v, w in graph_P:
        P.insert_edge(Vertex(u), Vertex(v), w)

    iter1 = [0]
    correctIsomorphism_1 = []
    M = Matrix((len(P.val), len(G.val)), 0)
    ullmann_v1([False] * len(G.val), 0, M, P, G, correctIsomorphism_1, iter1)
    print(len(correctIsomorphism_1), iter1[0])

    iter2 = [0]
    correctIsomorphism_2 = []
    M0 = create_M0(P, G)
    ullmann_v2([False] * len(G.val), 0, M0, P, G, correctIsomorphism_2, iter2)
    print(len(correctIsomorphism_2), iter2[0])

    iter3 = [0]
    correctIsomorphism_3 = []
    M0_v3 = create_M0(P, G)
    ullmann_v3([False] * len(G.val), 0, M0_v3, P, G, correctIsomorphism_3, iter3)
    print(len(correctIsomorphism_3), iter3[0])

if __name__ == '__main__':
    main()
