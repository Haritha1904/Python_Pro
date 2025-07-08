class inheritance():
    def __init__(self,Bookname,author):
        self.Bookname = Bookname
        self.author = author
    def display(self):
        print(f"Book name is {self.Bookname} and the author name is  : {self.author}")
        pass

class child1(inheritance):
    def __init__(self, Bookname, author,pages):
        super().__init__(Bookname, author)
         # here super method is used because we are inheriting from its parent class i.e inheritance
        self.pages = pages
    def display(self):
        super().display()
         # here super method is used because we are inheriting  the display details from its parent class i.e inheritance
        print(f"The no. of pages are :{self.pages}")

class child2(child1):
    def __init__(self, Bookname, author, pages,year):
        super().__init__(Bookname, author, pages)
         # here super method is used because we are inheriting from its parent class i.e child1
        self.year = year
    def display(self):
        super().display()
        # here super method is used because we are inheriting the display details from its parent class i.e child1
        print(f"The year published is in :{self.year}")
Obj1 = inheritance('Advaitha','Shankara')
Obj2 = child1('Advaitha','Shankara','100')
Obj3 = child2('Advaitha','Shankara','100','2003')
Obj3.display()