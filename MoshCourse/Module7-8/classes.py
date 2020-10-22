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
        self.age = 1

    def eat(self):
        print("eat")

# Animal: Parent, Base
# Mammal: Child, Sub
class Mammal(Animal):
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")


