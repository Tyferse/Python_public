import random


class Matrix:
    def __init__(self, iterable: list[list] = None):
        if not iterable:
            iterable = [[0]]
        
        self.__matrix_obj = list()
        self.size = (len(iterable), len(iterable[0]))
        for i in range(len(iterable)):
            if len(iterable[0]) != len(iterable[i]):
                raise MatrixSizeError(f"Number of elements in line {i}"
                                      " doesn't match number "
                                      "of elements in other lines.")
            
            self.__matrix_obj.append([])
            for j in range(len(iterable[0])):
                self.__matrix_obj[i].append(iterable[i][j])
                
    def __str__(self):
        s = "[["
        
        def add_this(ii, sz: tuple, mtrx):
            nonlocal s
            
            if ii != 0:
                s += ' ['
        
            if sz[1] > 10:
                s += ' '.join(str(c) for c
                              in mtrx[ii][:5])
                s += " ... "
                s += ' '.join(str(c) for c
                              in mtrx[ii][-5:])
            else:
                s += ' '.join(str(c) for c in mtrx[ii])
        
            if ii != sz[0] - 1:
                s += ']\n'
            
        if self.size[0] <= 10:
            for i in range(self.size[0]):
                add_this(i, self.size, self.__matrix_obj)
        else:
            for i in range(5):
                add_this(i, self.size, self.__matrix_obj)
                
            s += ' ... \n'
            for i in range(self.size[0] - 5, self.size[0]):
                add_this(i, self.size, self.__matrix_obj)
        
        s += ']]'
        return s
    
    def __len__(self):
        return self.size[0]
    
    def __getitem__(self, item):
        return self.__matrix_obj[item]
    
    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.size[1] != other.size[0]:
                raise MatrixMultiplyingError(
                    "Matrices can't be multiplied because of "
                    "their sizes (number of columns in left matrix "
                    f"{self.size[1]}"
                    "doesn't match number of rows in right matrix "
                    f"{other.size[0]}).")
            
            C = list()
            for i in range(self.size[0]):
                C.append([])
                for j in range(other.size[1]):
                    C[i].append(0)
                    for k in range(self.size[1]):
                        C[i][j] += self.__matrix_obj[i][k] * other[k][j]
            
            return Matrix(C)
        
        elif isinstance(other, (int, float)):
            self.__matrix_obj = [[other * self.__matrix_obj[i][j]
                                  for j in range(self.size[1])]
                                 for i in range(self.size[0])]
            return Matrix(self.__matrix_obj)
    
    def zeroes(self, size):
        if size < 1:
            raise MatrixSizeError("Size of matrix must be positive.")
        
        self.size = (size, size)
        self.__matrix_obj = [[0 for _ in range(size)]
                             for _ in range(size)]
    
    def unit(self, size: int):
        if size < 1:
            raise MatrixSizeError("Size of matrix must be positive.")
        
        self.size = (size, size)
        self.__matrix_obj = [[1 if i == j else 0
                              for j in range(size)]
                             for i in range(size)]
    
    def rand(self, rows, colomns, r=(0, 255)):
        if rows < 1 or colomns < 1:
            raise MatrixSizeError("Size of matrix must be positive.")
        
        self.size = (rows, colomns)
        self.__matrix_obj = [[random.randint(*r)
                              for _ in range(colomns)]
                             for _ in range(rows)]
    
    def T(self):
        mt = list()
        for i in range(self.size[1]):
            mt.append([])
            for j in range(self.size[0]):
                mt[i].append(self.__matrix_obj[j][i])
        
        self.__matrix_obj = mt
        return Matrix(self.__matrix_obj)
    
    @staticmethod
    def transpose(mtrx):
        mt = list()
        for i in range(len(mtrx[0])):
            mt.append([])
            for j in range(len(mtrx)):
                mt[i].append(mtrx[j][i])
                    
        return Matrix(mt)
    
    @staticmethod
    def minor(mtrx, rows: list, colomns: list):
        if len(mtrx) < 1:
            raise MatrixSizeError("There isn't minor of matrix "
                                  "with no elements")
        
        if len(rows) == len(colomns) == 1:
            return mtrx[rows[0]][colomns[0]]
            
        mn = list()
        line = 0
        for i in rows:
            mn.append([])
            for j in colomns:
                # print(line, i, j)
                mn[line].append(mtrx[i][j])
            
            line += 1
        
        return mn
    
    def determinant(self):
        if self.size[0] != self.size[1]:
            raise NotSquareMatrixError("There isn't determinant of "
                                       "not square matrix.")
        
        if self.size[0] == 2:
            return self.__matrix_obj[0][0] * self.__matrix_obj[1][1] \
                   - self.__matrix_obj[0][1] * self.__matrix_obj[1][0]
        
        elif self.size[0] > 2:
            d = 0
            for i in range(self.size[1]):
                if self.__matrix_obj[0][i] == 0:
                    continue
                
                cols = [j for j in range(self.size[1]) if j != i]
                
                d += (-1)**i * self.__matrix_obj[0][i] \
                             * self.minor_det(
                    self.minor(self.__matrix_obj,
                               list(range(1, self.size[0])), cols)
                )

                print(Matrix(self.minor(self.__matrix_obj,
                             list(range(1, self.size[0])), cols)))
                print((-1) ** i, '*', self.__matrix_obj[0][i], '*',
                      self.minor_det
                      (self.minor(self.__matrix_obj,
                                  list(range(1, self.size[0])), cols)
                       ))
            
            return d
    
    def minor_det(self, mn):
        d = 0
        if len(mn) > 2:
            for i in range(len(mn)):
                if mn[0][i] == 0:
                    continue

                cols = [j for j in range(len(mn[0])) if j != i]
                d += (-1)**i * mn[0][i] \
                             * self.minor_det(
                    self.minor(mn, list(range(1, len(mn[0]))), cols)
                )
                
                print(self.minor(mn, list(range(1, len(mn[0]))), cols))
                print((-1)**i, '*', mn[0][i], '*',
                      self.minor_det
                      (self.minor(mn, list(range(1, len(mn[0]))), cols))
                       )
            
            return d
        
        if len(mn) == 2:
            return mn[0][0] * mn[1][1] - mn[0][1] * mn[1][0]
    
    def mutual(self):
        mtrx = list()
        for i in range(self.size[0]):
            mtrx.append([])
            for j in range(self.size[1]):
                rs = [r for r in range(self.size[0]) if r != i]
                cs = [c for c in range(self.size[1]) if c != j]
                mtrx[i].append((-1)**(i + j) * self.minor_det(
                    self.minor(self.__matrix_obj, rs, cs)
                ))
                print(self.minor(self.__matrix_obj, rs, cs))
                print(self.minor_det(
                    self.minor(self.__matrix_obj, rs, cs)
                ))
        
        return Matrix(mtrx).T()


class MatrixSizeError(Exception):
    pass


class NotSquareMatrixError(Exception):
    pass


class MatrixMultiplyingError(Exception):
    pass


if __name__ == "__main__":
    A = Matrix([[0, -1, 1], [-5, -3, -2],
                [2, 5, -5]])
    # B = Matrix([[-13, 14, 11], [16, -22, -7], [-3, 9, -4]])
    print(A.mutual() * (1 / A.determinant()))
    # print(B.mutual())
    
    """
    A.unit(100)
    print(A.size, A.determinant())
    A.rand(4, 4, (0, 9))
    # print(A)
    print(A.determinant())
    A = Matrix([[4, 4, 5, 0], [7, 9, 4, 1], [8, 1, 2, 0], [2, 4, 2, 5]])
    # print(A)
    print(A.determinant())
    A.zeroes(80)
    print(A.determinant())
    
    A = Matrix([[1, 1, 2, 3], [0, 1, 1, 2],
                [0, 0, 1, 1], [0, 0, 0, 1]])
    B = Matrix([[3, 4, 9, 7], [1, 1, 7, 6],
                [7, 5, 7, 3], [2, 1, 3, 4]])
    print(A)
    """
