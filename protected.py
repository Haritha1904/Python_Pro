class protected:
    def __init__(self, name, age):
        self._name = name   # protected
        self._age = age     # protected

    def display(self):
        print("Name:", self._name)
        print("Age:", self._age)

# Creating object
s = protected("Haritha", 21)

# Accessing protected variables (allowed, but not recommended)
print("Accessing protected members from outside the class:")
print("Name:", s._name)
print("Age:", s._age)