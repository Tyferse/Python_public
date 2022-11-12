import doctest
import numba
import numpy
import random
import timeit


class Matrix(list):
    @classmethod
    def zeroes(cls, shape):
        n_rows, n_cols = shape
        return cls([[0] * n_cols for _ in range(n_rows)])

    @classmethod
    def random_m(cls, shape):
        M, (n_rows, n_cols) = cls(), shape
        for i in range(n_rows):
            M.append([random.randint(-255, 255) for _ in range(n_cols)])
            
        return M

    @property
    def shape(self):
        return (0, 0) if not self else (len(self), len(self[0]))


if __name__ == '__main__':
    m = Matrix()
    m = m.random_m((5, 5))
    print(m, m.shape, m.zeroes((5, 5)))


def matrix_product(x, y):
    """
    >>> x = Matrix([[1], [2], [3]])
    >>> y = Matrix([[4, 5, 6]])
    >>> matrix_product(x, y)
    [[4, 5, 6], [8, 10, 12], [12, 15, 18]]
    >>> matrix_product(y, x)
    [[32]]
    """
    n_xrows, n_xcols = x.shape
    n_yrows, n_ycols = y.shape
    z = Matrix.zeroes((n_xrows, n_ycols))
    for i in range(n_xrows):
        for j in range(n_xcols):
            for k in range(n_ycols):
                z[i][k] += x[i][j] * y[j][k]
                
    return z


if __name__ == '__main__':
    print(matrix_product(Matrix.random_m((4, 4)),
                         Matrix.random_m((4, 4))))
    doctest.testmod()
    setup = """
from Faster12 import Matrix, matrix_product
shape = 64, 64
x = Matrix.random_m(shape)
y = Matrix.random_m(shape)
    """
    print(timeit.timeit('matrix_product(x, y)', setup, number=10))


def bench(shape=(64, 64), n_iter=16):
    x = Matrix.random_m(shape)
    y = Matrix.random_m(shape)
    for it in range(n_iter):
        matrix_product(x, y)


def matrix_product(x, y):
    n_xrows, n_xcols = x.shape
    n_yrows, n_ycols = y.shape
    z = Matrix.zeroes((n_xrows, n_ycols))
    for i in range(n_xrows):
        xi, zi = x[i], z[i]
        for j in range(n_xcols):
            z[i][j] = sum(xi[k] * y[k][j] for k in range(n_xcols))
            
    return z


if __name__ == '__main__':
    setup = """
from Faster12 import Matrix, matrix_product
shape = 64, 64
x = Matrix.random_m(shape)
y = Matrix.random_m(shape)
    """
    print(timeit.timeit('matrix_product(x, y)', setup, number=20))


x = numpy.random.randint(-255, 255, (64, 64))
y = numpy.random.randint(-255, 255, (64, 64))
print(x.dot(y))


@numba.jit
def jit_matrix_product(x, y):
    n_xrows, n_xcols = x.shape
    n_yrows, n_ycols = y.shape
    z = numpy.zeros((n_xrows, n_ycols), dtype=x.dtype)
    for i in range(n_xrows):
        for k in range(n_ycols):
            for j in range(n_xcols):
                z[i, k] += x[i, j] * y[j, k]
                
    return z


print(jit_matrix_product(numpy.random.randint(-255, 255, (64, 64)),
                         numpy.random.randint(-255, 255, (64, 64))))


@numba.jit
def jit_matrix_product(x, y):
    n_xrows, n_xcols = x.shape
    n_yrows, n_ycols = y.shape
    z = numpy.zeros((n_xrows, n_ycols))
    for i in range(n_xrows):
        for k in range(n_ycols):
            z[i, k] = (x[i, :] * y[:, k]).sum()
            
    return z


print(jit_matrix_product(numpy.random.randint(-255, 255, (64, 64)),
                         numpy.random.randint(-255, 255, (64, 64))))
