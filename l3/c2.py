#3 Define a class named Rectangle which inherits from Shape class from task 2. 
#Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.
class Shape():
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Rectangle(Shape):
    def area(self):
        print(self.length * self.width)

x = int(input())
y = int(input())
s = Rectangle(x, y)
s.area()

#4 Point class
#a method show to display the coordinates of the point
#a method move to change these coordinates
#a method dist that computes the distance between 2 points

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(self.x, end = " ")
        print(self.y)
    
    def move(self, x1, y1):
        self.x += x1
        self.y += y1
        print(self.x, end = " ")
        print(self.y)
    
    def dist(self, Point):
        print(abs(Point.x - self.x), end = " ")
        print(abs(Point.y - self.y))

p1 = Point(6, 8)
p2 = Point(5, 5)
p1.show()
p1.move(1, 1)
p1.dist(p2)

