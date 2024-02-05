class shape():
    def __init__(self):
        pass
    def area(self):
        print(0)

class rectangle(shape):
    def __init__(self, length, weigth):
        super().__init__()
        self.length = length
        self.weigth = weigth
    def area(self):
        print(self.weigth * self.length)

r1 = rectangle(3, 5)
r1.area()