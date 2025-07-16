class Robot():
    def __init__(self,name):
        self.name = name
        self.position = 0
    def move_forward(self,steps):
        self.position+= steps
        print(f"{self.name}moved forward {steps} no. of steps and its position is {self.position}")
    def move_backward(self,steps):
        self.position-= steps
        print(f"{self.name}moved backward {steps} no. of steps and its position is {self.position}")
Object = Robot('Haritha Bot')
Object.move_forward(6)
Object.move_backward(3)