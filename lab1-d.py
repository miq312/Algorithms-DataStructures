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
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])
    
    def size(self):
        return len(self.matrix), len(self.matrix[0])
    
    def swap_rows(self, row1, row2):
        self.matrix[row1], self.matrix[row2] = self.matrix[row2], self.matrix[row1]
    
def det_2x2(matrix: Matrix) -> float:
    return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

def chio(matrix: Matrix, value: float = 1) -> float:
    if matrix.size() == (2,2):
        return value * det_2x2(matrix)
    
    if matrix[0][0] == 0:
        for i in range(matrix.size()[0]):
            if matrix[i][0] != 0:
                matrix.swap_rows(0, i)
                value *= -1
                break
        else:
            return 0
    
    new_value = value * 1 / matrix[0][0] ** (matrix.size()[0] - 2)

    matrix_reduced = []
    for i in range(matrix.size()[0] - 1):
        new_row = []
        for j in range(matrix.size()[0] - 1):
            new_row.append(det_2x2(Matrix([[matrix[0][0], matrix[0][j+1]], [matrix[i+1][0], matrix[i+1][j+1]]])))
        matrix_reduced.append(new_row)

    return chio(Matrix(matrix_reduced), new_value)

def main():
    A = Matrix([[5, 1, 1, 2, 3],
                [4, 2, 1, 7, 3],
                [2, 1, 2, 4, 7],
                [9, 1, 0, 7, 0],
                [1, 4, 7, 2, 2]])
    B = Matrix([[0, 1, 1, 2, 3],
                [4, 2, 1, 7, 3],
                [2, 1, 2, 4, 7],
                [9, 1, 0, 7, 0],
                [1, 4, 7, 2, 2]])
    
    print(chio(A))
    print(chio(B))

if __name__ == "__main__":
    main()