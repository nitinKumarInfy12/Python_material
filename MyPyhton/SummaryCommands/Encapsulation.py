class car:

    # "__" double underscore is used to create data private

    def __init__(self, color, speed): # default value
        self.color = color
        self.speed = speed

# for encapsulation we create functions and private data, setter / getter methods
    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed



ford = car('Red',220)
toyota = car('green', 240)

ford.set_speed(300)
ford.speed = 400

print(ford.get_speed())
print(ford.color)

#================================== private data==========================
print("================================== private data==========================")
class car1:

    # "__" double underscore is used to create data private
    # var : is a public member variable
    # __var : is a private member variable. cannoyt be accessible ooutside teh class, but all methods inside teh class can access teh private variables to tehe class
    # __MethodName : is teh private method to class : it cannot be accessed outside teh class
    # use self keyword to call a private method inside teh class. self.__MethodName

    def __init__(self, color, speed): # default value
        self.__color = color
        self.__speed = speed


# for encapsulation we create functions and private data
    def set_speed(self, speed):  # getter method
        self.__speed = speed

    def get_speed(self): # settor method
        return self.__speed



ford = car1('Red',220)
toyota = car1('green', 240)

ford.set_speed(300)
ford.__speed = 400 # this will not throw error but wont do anything

print(ford.get_speed())
# print(ford.__color)  # this will throw error, because the variable cannot be accessed directly from outside



