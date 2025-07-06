class fact():
    def __init__(self,num):
        self.num=num
    def Calc_Factorial(self):
        factorial = 1
        if  self.num < 0 :
            print("Fact not found for -ve")
        elif self.num==0 or self.num==1 :
            print("Fact is 1")
        else:
            for i in range(2,self.num+1):
                factorial *= i
            return factorial
A = fact(-8)
print(A.Calc_Factorial())


        
        