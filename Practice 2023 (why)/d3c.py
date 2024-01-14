class Polynomial:
    def __init__(self, coefficients):
        self.coeff = coefficients
    
    def __add__(self, other):
        ml = max(len(self.coeff), len(other.coeff))
        new_cf = [0] * ml
        for i in range(len(self.coeff)):
            new_cf[i] += self.coeff[i]
        
        for i in range(len(other.coeff)):
            new_cf[i] += other.coeff[i]
    
        return Polynomial(new_cf)
    
    def __call__(self, x):
        if len(self.coeff) == 1:
            return self.coeff[0]
        
        res = self.coeff[-1] * x + self.coeff[-2]
        for i in range(-3, -len(self.coeff) - 1, -1):
            res = res * x + self.coeff[i]
            
        return res


poly = Polynomial([10, -1])
print(poly(0))
print(poly(1))
print(poly(2), end='\n\n')

poly1 = Polynomial([0, 1])
poly2 = Polynomial([10])
poly3 = poly1 + poly2
poly4 = poly2 + poly1
print(poly3(-2), poly4(-2))
print(poly3(-1), poly4(-1))
print(poly3(0), poly4(0))
print(poly3(1), poly4(1))
print(poly3(2), poly4(2))
