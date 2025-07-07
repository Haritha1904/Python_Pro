class Grade():
    def __init__(self,mark):
        self.mark = int(mark)
    def check(self):
        if self.mark > 30 :
            print("Pass")
        else:
            print("Fail")
A= Grade('45')
A.check()
        