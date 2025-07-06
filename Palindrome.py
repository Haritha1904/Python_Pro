class Palindrome():
    def __init__(self,str):
        self.str = str
    def Chk_Palindrome(self):
        if self.str == self.str[::-1]:
            print("Yes its a Palindrome")
        else:
            print("Not a Palindrome")
Obj = Palindrome('madam')
Obj.Chk_Palindrome()