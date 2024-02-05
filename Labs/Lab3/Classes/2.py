class shape():
    def __init__(self):
        pass
    def area(self):
        print(0)

class square(shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        print(self.length**2)
    
s0 = shape()
s1 = square(5)
s1.area()
s0.area()
        
    



