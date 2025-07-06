class Class_Obj():
    def __init__(self,a='Demo'):
        self.a = a
    def basic(self):
        print(f"You are inside a {self.a} class") 
        # to print the string stored in self.a
Var = Class_Obj()
Var.basic()
        