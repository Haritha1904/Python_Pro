class Big():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def Biig(self):
        if((self.a>self.b) and (self.a>self.c)):
            print("A is Biggest amongst the three variables")
        elif(self.b > self.a and self.b > self.c):
            print("B is big")
        else:
            print("c is Big")
        
a = Big(99,2,456)
a.Biig()
