class Ascii():
    def __init__(self,character):
        self.ch = character
    def Asc(self):
        result = ord(self.ch)
        print(result)
a = Ascii('D')
a.Asc()
