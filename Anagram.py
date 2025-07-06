class Anagram():
    def __init__(self,str1,str2):
        self.str1 = str1
        self.str2 = str2 
    def Ana(self):
        if sorted(self.str1) == sorted(self.str2):
            print(" they are Anagrams ")
        else:
            print("they are not ")
a=Anagram("Hari","arHi")
a.Ana()
        
