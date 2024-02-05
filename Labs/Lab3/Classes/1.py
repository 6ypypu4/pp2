class my_class():
    def __init__(self):
        self.string = "Print smth"
    def getString(self, my_string):
        self.string = my_string
    def printString(self):
        print(self.string)


s1 = my_class()
s1.getString(input())
s1.printString()

