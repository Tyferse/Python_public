class Balance:
    def __init__(self):
        self.blnc = 0
    
    def add_right(self, weight):
        self.blnc += weight
    
    def add_left(self, weight):
        self.blnc -= weight
    
    def result(self):
        if self.blnc == 0:
            return '='
        else:
            return 'L' if self.blnc < 0 else 'R'


balance = Balance()
balance.add_right(10)
balance.add_left(5)
balance.add_left(5)
print(balance.result())
balance.add_left(1)
balance.add_right(2)
print(balance.result())
