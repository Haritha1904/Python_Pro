class concat():
    def __init__(self,str1,str2):
        self.str1 = str1
        self.str2 = str2
    def let_Concat(self):
        Concated_String = self.str1 + self.str2
        print(Concated_String)
A = concat('Hari','tha')
A.let_Concat()