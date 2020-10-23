# Module 7: Classes
# Class: Blueprint for creating new objects
# Object: Instance of a class

# Class: Human
# Object: John, Mary, Jack


class Point:
    # Define things in the block

    # Constructor magic method
    def __init__(self, x, y):
        # Self is reference to current Point object
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    @classmethod
    def zero(cls):
        # Same as Point(0, 0)
        return cls(0, 0)


    def draw(self):
        print(f'Point ({self.x}, {self.y})')

# pointa = Point(1, 2)
# pointb = Point(1, 2)
# pointc = Point(10, 20)
# pointd = Point(10, 19)
# combined = pointa + pointb
# print(pointa == pointb)
# print(pointc > pointd)
# print(pointa + pointc)
# print(combined.x)
#
# point1 = Point(1, 2)
# point1.draw()
# print(str(point1))
#
# point2 = Point(3, 4)
# point2.draw()
#
# point3 = Point.zero()
# point3.draw()




class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        # Returns one item at a time in a for loop
        return iter(self.__tags)

# cloud = TagCloud()
# cloud["python"] = 10
# len(cloud)
# cloud.add("Python")
# cloud.add("python")
# cloud.add("python")
# print(cloud.__tags)



class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

# product = Product(-10)
# print(product.price)

class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")

# Animal: Parent, Base
# Mammal: Child, Sub
class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal Constructor")
        self.weight = 1

    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")


# m = Mammal()
# print(m.age)
# print(m.weight)

# Good example of multiple inheritance
class Flyer:
    pass

class Swimmer:
    pass

class FlyingFish(Flyer, Swimmer):
    pass


# Good example of Inheritance
from abc import ABC, abstractmethod

class InvalidOperationError(Exception):
    pass

class Stream(ABC):
    def __init__(self):
        self.open = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")

class FileStream(Stream):
    def NetworkStream(self):
        print("Reading data from a network")

class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream.")


# Polymorphism Example -----
# Rendering user interface example
# Can allow work without the UIControl class and it's references

class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass

class TextBox(UIControl):
    def draw(self):
        print("TextBox Drawn")

class DropDownList(UIControl):
    def draw(self):
        print("DropDownList Drawn")

def draw(controls):
    for ui in controls:
        ui.draw()

# ddl = DropDownList()
# textbox = TextBox()
# draw([ddl, textbox])


# Extending Built-in Types

class Text(str):
    def duplicate(self):
        return self + self

class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)

# text = Text("Python")
# print(text.duplicate())
#
# list = TrackableList()
# list.append("1")


class PointA:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def PointCalc():
    p1 = PointA(1, 2)
    p2 = PointA(1, 2)
    print(p1 == p2)
PointCalc()

from collections import namedtuple

PointZ = namedtuple("Point", ["x", "y"])
p1 = PointZ(x=1, y=2)
p2 = PointZ(x=1, y=2)
# p1 and p2 are immutable
print(p1 == p2)

