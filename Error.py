class Error(Exception): # it means that we have created a class named Error and it is inheriting from Exception 
    # def __init__(self,balance):  not required because try,except cannot be placed directly inside the main init so create another class
    #     self.balance = balance = 3000
    pass
class Balance():
    def __init__(self):
        self.balance = 3000
        print(f"The balance is : {self.balance}")
        pass
    def wd_amount(self):
        self.amount = 1000
        #try block is where the error can occur
        try:        
            if self.amount <= 0:
                raise ValueError("Withdrawl amount should be > 0")
            if self.amount >self.balance:
                raise Error("Insufficient balance") # the word Error here is a custom Exception that we created in the class both should be same 
            else:
                self.balance = self.balance - self.amount
                
                print(f"Thee amount withdrawn is : {self.amount}")
                print(f"The balance is :{self.balance}")

        except ValueError as ve:
            print(f"invalid input : {ve}")
        except Error as e:
            print(f"insufficient balance : {e}")
        finally:
            print("Thank you")
Obj1 = Balance()
Obj1.wd_amount()

