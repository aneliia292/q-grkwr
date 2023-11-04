class Shape:


    def __init__(self, name, color):


        self.name = name
        self.color = color


def describe(self):


    print (f"This shape is a {self.color} {self.name}")


class Circle (Shape):


    def __init__(self, name, color, radius):


        super ().__init__ (name, color)
        self.radius = radius


def area(self):


    return 3.14159 * self.radius ** 2


class Rectangle (Shape):


    def __init__(self, name, color, length, width):


        super ().__init__ (name, color)
        self.length = length
        self.width = width


def area(self):


    return self.length * self.width


class Triangle (Shape):


    def __init__(self, name, color, base, height):


        super ().__init__ (name, color)
        self.base = base
        self.height = height


def area(self):


    return 0.5 * self.base * self.height

# Пример использования классов
circle = Circle ("Circle", "red", 5)
circle.describe ()
print ("Area:", circle.area ())

rectangle = Rectangle ("Rectangle", "blue", 4, 6)
rectangle.describe ()
print ("Area:", rectangle.area ())

triangle = Triangle ("Triangle", "green", 3, 5)
triangle.describe ()
print ("Area:", triangle.area ())
