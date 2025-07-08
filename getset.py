class getset():
    def __init__(self):
        self.__mark = 0
    def get_marks(self):  # getter
        print(self.__mark)
    def set_marks(self,mark):
        if 0 < mark <100:
            self.__mark = mark
            print(f"Marks is : {self.__mark}")
        else:
            print("Invalid mark")
A = getset()
A.get_marks()
A.set_marks(30)
