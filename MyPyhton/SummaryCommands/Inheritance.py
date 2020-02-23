# super class
# sub class : inherits from super class, it can add its own methods on top of it.
# note: sub class cannot access teh private members of teh super class, to overcome this need to create publi setter/getter methods in teh Super class
# is-are relationship

class Polygon:

     __height = None
     __width = None

     def set_values(self, height, width):
         self.__height = height
         self.__width = width

     def get_height(self):
         return self.__height

     def get_width(self):
         return self.__width



class Rectangle(Polygon): # here rectangle class is inheriting from the Polygon class
    def area(self):
        # return self.__height*self.__width  # it will not work as sub class cannot access private members of teh super class
        return self.get_height() * self.get_width()


class Traingle(Polygon):
    def area(self):
        # return self.__height*self.__width / 2 # it will not work as sub class cannot access private members of teh super class
        return self.get_height() * self.get_width()



rect = Rectangle() # initiate the rect instance of teh rectangle class
trai = Traingle() # initiate the rect instance of teh rectangle class

rect.set_values(50,40)
trai.set_values(50,40)

print(rect.area())
print(trai.area())



# multiple inheritance
#class ClassName(class1,class2):