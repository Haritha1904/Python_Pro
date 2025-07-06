class Calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self) : print(self.a + self.b)
    def sub(self) : print(self.a - self.b)
    def mul(self) : print (self.a * self.b)
    def div(self) : print (self.a // self.b)
    
A=Calculator(2,2)
A.sum()
A.sub()
A.mul()
A.div()