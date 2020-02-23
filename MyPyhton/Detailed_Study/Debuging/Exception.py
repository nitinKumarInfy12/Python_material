#! python3

# functions would have raise Exception statements with some exception message
# code must have try-except block to handle the execution an dexception else the code will throw error
# you can obtain the exception as a string by calling traceback.format_exc()

# import builtins
# help (builtins) will give the list of available builtin exceptions


class CoffeeCup:
    def __init__(self, temperature):
        self.__temperature = temperature

    def drink_coffee(self):
        if self.__temperature > 85:
            #print("Its too hot to drink")
            raise Exception("Its too hot to drink")
        elif self.__temperature < 65:
            #print("Its too cold to drink")
            raise Exception("Its too cold to drink")
        else:
            print("Its ok to drink")

try:
    cup = CoffeeCup(87)
    print(cup.drink_coffee())
except Exception as err:
    print('An exception happened: ' + str(err))

# we can add Else and Finalle too to the try-except block

else: # else statement will not be executed whenever there is any exception
    print ('__else__')
finally: # it is gu')ranteed to execute, dosent matter error occurs or not
    print ('__finally__')

print("Program continued...")