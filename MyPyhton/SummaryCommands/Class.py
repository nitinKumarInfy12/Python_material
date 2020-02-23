# objects in Python are instance of Class

# items/data within class are called attributes

# functions within class are called Methods

# objects can interchange data between multiple objects
#ex:
"""
class Cab{ # object of cab class
    CabService, Make, Location, # data
    Book(), CabType(), arrival() # methods

}
"""
# empty class
class Car:
    pass # it can be used to create empty method as well

# instance / object of the class
ford = Car()
honda = Car()
toyota = Car()

# add th attributes/data to teh objects.
ford.speed = 200
honda.speed = 220
toyota.speed = 240

ford.color =  'white'
honda.color = 'red'
toyota.color = 'blue'

print (ford.color)

ford.color = 'green'

print (ford.color)


