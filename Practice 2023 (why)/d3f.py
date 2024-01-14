class Summator:
    def __init__(self):
        pass
    
    def transform(self, n):
        return n

    def sum(self, n):
        return sum(self.transform(i) for i in range(1, n + 1))


class SquareSummator(Summator):
    def transform(self, n):
        return n**2


class CubeSummator(Summator):
    def transform(self, n):
        return n**3


s = Summator()
ssq = SquareSummator()
scb = CubeSummator()
print(s.sum(5))
print(ssq.sum(5))
print(scb.sum(5))
