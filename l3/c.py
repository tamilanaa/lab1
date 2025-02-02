#1 Define a class which has at least two methods: getString: to get a string from console input printString: 
# to print the string in upper case.
class asd():
    def __init__(self):
        self.str = ""

    def getString(self):
        self.str = input("Enter a string: ")

    def printString(self):
        print(self.str.upper()) 
a = asd()

a.getString()
a.printString()

#Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. 
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
      
class Shape():
    def __init__(self, length):
        self.length = length
    def area(self):
        print(0)

class Square(Shape):
    def area(self):
        print(self.length * self.length)

a = int(input())
b = Shape(a)
b.area()
b = Square(a)
b.area()
      