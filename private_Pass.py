class private_Pass():
    def __init__(self,password):
        self.__password = password #it means password is a private variable
    def login(self,yourpassword):
        # print(f"In class private variable can be accesed : see {self.__password}")
        if self.__password == yourpassword :
            print(f"The password {yourpassword} is correct ")
        else:
            print("Password Invalid")
A = private_Pass('Hari')
A.login('Shri')
A.login('Hari')
# print(yourpassword)
print(A._private_Pass__password) # here we are trying to access the private variable outside the class
# this method basically is called as Name Mangling
# syntax for this is <<Obj name>>._<<Classname>>__<<Private variable name>>