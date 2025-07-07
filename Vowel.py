class Vowel():
    def __init__(self,ch):
        self.ch = ch
    def Find(self):
        vowels = ['a','e','i','o','u']
        for i in vowels:
            if self.ch == i:
                print("Vowels")
                break
            else:
                print("Consonants")
                break
A = Vowel('b')
A.Find()
        