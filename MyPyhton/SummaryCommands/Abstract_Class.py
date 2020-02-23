# abstract class: You donot want to allow users to create instance of the class
# to create a class need to create abstract method in teh class by using the decorators "@abstractmethod" for the abstract method
# import teh ABC module in the class to maki it abstract and the decorator to make the method abstract
# Abstract methods of teh super class must be implemented in teh sub class

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return 4 * self.__side

# shape  = Shape()  # since the Shape class is now abstract class it can not be instantiate
square = Square(5)
print (square.area())
print(square.perimeter())




