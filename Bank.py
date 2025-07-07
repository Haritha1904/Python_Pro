class Bank():
    def __init__(self,balance = '0'):
        self.balance = int(balance)
        
    def deposit(self,amount):
        self.balance = self.balance + amount 
        print(f"Amount deposited :{amount} ")
        print(f"total :{self.balance} ")
    def withdraw(self,amount):
        if self.balance >= amount :
            self.balance = self.balance - amount 
            print(f"Amount withdrawn :{amount} ")
            print(f"Balance is: {self.balance}") 
        else:
            print("Balance insufficient to withdraw")
A= Bank('10')
A.deposit(20)
A.withdraw(5)

        