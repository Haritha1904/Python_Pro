from abc import ABC , abstractmethod  # it is the syntax for abstract class 
# here abc is module ABC is Abstract Base class
#Obj cannot be created from abstract class ,
#-holds only abstract methods min 1
#-the sub classes should inhert the method from the abstract class 
#-method implementation to be done only in subclases

class abstract(ABC):
    @abstractmethod
    def area(self):
        pass
class circle():
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print(f" area of circle is : {3.14 * self.radius *self.radius}")
        pass
class rect():
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        print(f" area of rectangle  is : {self.l *self.b}")
        pass

Obj1 = circle(2)
Obj2 = rect(4,3)

Obj1.area()
Obj2.area()





    