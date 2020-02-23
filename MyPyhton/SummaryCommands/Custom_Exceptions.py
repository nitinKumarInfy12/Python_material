# to create custom excepption class, need to inherit the Exception class

class CofeeeTooHotException(Exception):
    def __init__(self, message):
        super().__init__(message)

class CoffeeTooColdException(Exception):
    def __init__(self, message):
        super().__init__(message)

class CoffeeCup:
    def __init__(self, temperature):
        self.__temperature = temperature

    def drink_coffee(self):
        if self.__temperature > 85:
            #print("Its too hot to drink")
            raise CofeeeTooHotException("Its too hot to drink, coffe temeparture :" + str(self.__temperature))
        elif self.__temperature < 65:
            #print("Its too cold to drink")
            raise CoffeeTooColdException("Its too cold to drink, coffe temeparture :" + str(self.__temperature))
        else:
            print("Its ok to drink")

cup = CoffeeCup(87)
print(cup.drink_coffee())
