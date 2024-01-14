class MyVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'MyVector({self.x}, {self.y})'
    
    def __add__(self, other):
        return MyVector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return MyVector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        assert isinstance(other, (int, float))
        return MyVector(self.x * other, self.y * other)
    
    def __rmul__(self, other):
        return self * other
    
    def __imul__(self, other):
        self.x *= other
        self.y *= other
        return self

    def __eq__(self, other):
        return self.x == other.x and self.y == self.y
    
    def __ne__(self, other):
        return self.x != other.x or self.y != self.y
    
    def __abs__(self):
        return (self.x**2 + self.y**2)**.5


v1 = MyVector(-2, 5)
v2 = MyVector(3, -4)
v_sum = v1 + v2
print(v_sum)
print(abs(v_sum))
print(v1 - v2)
print(v_sum * 2.5)
v1 *= 1/2
print(3 * v1)
print(v1 != v2, v_sum == v2)
