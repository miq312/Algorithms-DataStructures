#skonczone
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
        if self.size()[0] != other.size()[1]:
            raise Exception("Mul::Wrong matrix shape")
        else:
            matrix_mul = [[0] * other.size()[1] for _ in range(self.size()[0])]

            for i in range(self.size()[0]):
                for j in range(other.size()[1]):
                    for k in range(self.size()[1]):
                        matrix_mul[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return Matrix(matrix_mul)
                
    def __getitem__(self, index):
        return self.matrix[index]

    def __str__(self):
        matrix_str = ""
        for row in self.matrix:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str
    
    def size(self):
        return len(self.matrix), len(self.matrix[0])
     
def transpose(matrix: Matrix) -> Matrix: 
    n = matrix.size()[0]
    m = matrix.size()[1]

    matrix_tr = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            matrix_tr[j][i] = matrix[i][j]
    return Matrix(matrix_tr)

def main():

    m1 = Matrix([ [1, 0, 2], [-1, 3, 1] ])
    m2 = Matrix((2, 3), 1)
    m3 = Matrix([ [3, 1], [2, 1], [1, 0] ])
    
    print(transpose(m1))
    print(m1+m2)
    print(m1*m3)

if __name__ == "__main__":
    main()
