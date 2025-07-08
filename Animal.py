class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        # super().sound()
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        # super().sound()
        print("Cat meows")

# Polymorphism in action
def make_sound(animal): #this is used to call the required method 
    animal.sound()

a = Animal()
d = Dog()
c = Cat()

make_sound(a)
make_sound(d)
make_sound(c)

