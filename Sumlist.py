class Sumlist():
    def __init__(self,numbers):
        self.numbers = numbers
    def Calc_Sum(self):
        total = 0
        for num in self.numbers:
            total += num
            print(total)
List = [1,2,3,4,5]   
a = Sumlist(List)
a.Calc_Sum()