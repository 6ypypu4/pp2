class Point():
    def __init__(self, x, y, z):
        self.x = x
        self.z = z
        self.y = y
    def show(self):
        print(self.x ,self.y, self.z)
    def move(self, x, y, z):
        self.x += x
        self.z += z
        self.y += y
    def dist(self, other_point):
        return ((self.x - p2.x)**2 + (self.y - p2.y)**2 + (self.z - p2.z)**2 )**0.5


p1 = Point(1, 1, 1)
p2 = Point(3, 1, 1)
p1.show()
p1.show()
print(p1.dist(p2))
