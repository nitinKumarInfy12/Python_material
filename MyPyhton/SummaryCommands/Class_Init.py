class Rectanggle:
    #pass # to create an empty class

    def __init__(self): # served as constructor of the class. it is teh first statement wil be called for any class/object
       print('the __init__(self) is called')

###### Method
## for every method inside a class first argument must be self(or any keyword used as self) to initialize teh method

# select the rows and click on Ctrl + / to comment all teh selected rows

# rect1 = Rectanggle()
# rect2 = Rectanggle()
#
# rect1.height = 20
# rect1.width = 30
#
# rect2.height = 40
# rect2.width = 50
#
# print(rect1.height * rect1.width)
# print(rect2.height * rect2.width)

######################################################################

class car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
        #print(speed)
        #print(color)


ford = car('Red',200) # object of teh car class
honda = car('Blue',220)

print(ford.color)
print(honda.speed)

################################################################################
class Square:
    def __init__(abc, height, width):
        abc.height = height
        abc.width = width
        print ("area of the Square :", abc.height * abc.width)

sqr1 = Square(20,22)







