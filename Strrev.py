class Strrev():
    def __init__(self,str):
        self.str = str
    def Reverse(self):
        return self.str[::-1]
    # to reverse a given string use [::-1]
string = Strrev('Haritha')
print(string.Reverse())