## class should be Pascal case
## Method must have one parameter 
## self - if instance method
## cls - if class method
## Google it for magic methods; predefined methods for best use


class MyClass:
    def IsInstanceMethod(self):
        return "this is instance method & 'self' have instance reference "
    
    @classmethod     ## use this decorator to identify/specify class methods
    def isClassMethod(cls):
        return "this is static/ Class method & 'cls' have class reference"


class Point:
    default_color = "Green"  ## Class attribute; can be access with class name or any instance of this class

    def __init__(self, x, y): ## __init__ is constructor method
        self.x = x  ## instance attribute;  can be access only with this instance
        self.y = y

    @classmethod
    def changeDefaultColor(cls, sNewColor):
        cls.default_color = sNewColor

    def draw(self):
        return f"draw(Point({self.x}, {self.y}), {self.default_color})"


point_1 = Point(2,5)
print(point_1.draw())

point_2 = Point(3,6)

Point.changeDefaultColor("Red")

print(point_1.draw())
print(point_2.draw())

##--------------------------------------------------------
## Comparing Objects && Magic Methods
##--------------------------------------------------------
print("Comparing Objects && Magic Methods")
class MyPoint:
    default_color = "Green"  ## Class attribute; can be access with class name or any instance of this class

    def __init__(self, x, y): ## __init__ is constructor method
        self.x = x  ## instance attribute;  can be access only with this instance
        self.y = y

    @classmethod
    def changeDefaultColor(cls, sNewColor):
        cls.default_color = sNewColor

    def draw(self):
        return f"draw(Point({self.x}, {self.y}), {self.default_color})"

    def __eq__(self, Other): # Magic method for comparing Equel '==' ; this method will call when compare objct with '=='
        return self.x == Other.x and self.y == Other.y
    
    def __gt__(self, Other): # Magic method for comparing Gretethan '>' ; this method will call when compare objct with '>'
        return self.x > Other.x and self.y > Other.y

point_1 = MyPoint(5, 10)
point_2 = MyPoint(5, 10)

## Compare Object
print("lessthan <", point_1 < point_2)  # first will compare with second object

## for object == will complere with reference; there would be always false
print("Equal To =", point_1 == point_2) #  will call __eq__ method of point_1 instance

print("Greterthan >", point_1 > Point(1, 2)) # will call __gt__ method of point_1 instance

##---------------------------------------------------------
## Arithmetic Operator && Numeric Magic Methods
##--------------------------------------------------------
print("Arithmetic Operator && Numeric Magic Methods")
class Counter():
    def __init__(self, sNumber):
        self.counter = sNumber
    
    def __add__(self, Other): # Magic method for Arithmetic Operator '+'
       return Counter(self.counter + Other.counter) # Return new instance with add two values
    
    def __mul__(self, Other): # Magic method fro Arithmetic Operator '*'
        return Counter(self.counter * Other.counter)
    
    def getCounter(self):
        return self.counter
    
    def incrementCounter(self):
        self.counter += 1


counter_1 = Counter(5)
counter_2 = Counter(10)

counter_3 = counter_1 + counter_2
print("add +", counter_3.getCounter())

counter_4 = counter_1 * counter_2
print("mul *", counter_4.getCounter())

try:
    counter_3 = counter_1 - counter_2 ## no magic method implemented for substact '-'
except TypeError as ex:
    print(ex)