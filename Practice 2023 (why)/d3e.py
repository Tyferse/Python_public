class Queue:
    def __init__(self, *args):
        assert len(args) > 0
        self.q = list(args)
    
    def __str__(self):
        return '[' + ' -> '.join(str(i) for i in self.q) + ']'
    
    def append(self, *values):
        assert len(values) > 0
        self.q.extend(values)
    
    def copy(self):
        return Queue(*self.q)
    
    def pop(self):
        if len(self.q) == 0:
            return None
        
        el = self.q[0]
        # del self.q[0]
        self.q = self.q[1:]
        return el
    
    def extend(self, other):
        self.q.extend(other.q)
    
    def next(self):
        assert len(self.q) > 0
        return Queue(*self.q[1:])
    
    def __add__(self, other):
        return Queue(*(self.q + other.q))
    
    def __iadd__(self, other):
        self.extend(other)
        return self
    
    def __eq__(self, other):
        assert len(self.q) == len(other.q)
        return all(a == b for a, b in zip(self.q, other.q))
    
    def __next__(self):
        return self.next()
    
    def __rshift__(self, n):
        if n >= len(self.q):
            return Queue()
        
        return Queue(*self.q[n:])


q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)
qx = q1.copy()
print(qx.pop())
print(qx)
q2 = q1.copy()
print(q2)
print(q1 == q2, id(q1) == id(q2))
q3 = q2.next()
print(q1, q2, q3, sep='\n')
print(q1 + q3)
q3.extend(Queue(1, 2))
print(q3)
q4 = Queue(1, 2)
q4 += q3 >> 4
print(q4)
q5 = next(q4)
print(q4)
print(q5)
