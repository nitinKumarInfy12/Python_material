#When Python encounters an error, it produces a treasure trove of error information called
#the traceback. The traceback includes the error message, the line number of the line that
##caused the error, and the sequence of the function calls that led to the error. This sequence
#of calls is called the call stack.
# # you can obtain the exception as a string by calling traceback.format_exc() of traceback module
# print (50/ 0) # Throws error :" ZeroDivisionError: division by zero
# print (10 + '10') # eception : " TypeError: unsupported operand type(s) for +: 'int' and 'str'

"""
# import builtins
# help (builtins)


CLASSES
    object
        BaseException
            Exception
                ArithmeticError
                    FloatingPointError
                    OverflowError
                    ZeroDivisionError
                AssertionError
                AttributeError
                BufferError
                EOFError
                ImportError
                    ModuleNotFoundError
                LookupError
                    IndexError
                    KeyError
                MemoryError
                NameError
                    UnboundLocalError
                OSError
                    BlockingIOError
                    ChildProcessError
                    ConnectionError
                        BrokenPipeError
                        ConnectionAbortedError
                        ConnectionRefusedError
                        ConnectionResetError
                    FileExistsError
                    FileNotFoundError
                    InterruptedError
                    IsADirectoryError
                    NotADirectoryError
                    PermissionError
                    ProcessLookupError
                    TimeoutError
                ReferenceError
                RuntimeError
                    NotImplementedError
                    RecursionError
                StopAsyncIteration
                StopIteration
                SyntaxError
                    IndentationError
                        TabError
                SystemError
                TypeError
                ValueError
                    UnicodeError
                        UnicodeDecodeError
                        UnicodeEncodeError
                        UnicodeTranslateError
                Warning
                    BytesWarning
                    DeprecationWarning
                    FutureWarning
                    ImportWarning
                    PendingDeprecationWarning
                    ResourceWarning
                    RuntimeWarning
                    SyntaxWarning
                    UnicodeWarning
                    UserWarning
            GeneratorExit
            KeyboardInterrupt
            SystemExit


"""


# it require to use "try- except " for teh exception handling
# else and finally , can also be added to teh try-except block
# else : it executes only when there is no error/exception
# finally: it executes guranteed, no matter eroor was occured or not
# raise : statement forces the program to raise an exception. it can use Exception class or any sub class of teh Exception class

print ("=====================================Exception handliog ======================================================")

result = None

a = float(input("provide the numerator :"))
b = float(input("Provide teh denominator :"))

try: # write the code in the try block
    result = a / b

# This is a generic exception handling, we can use the buitlin exceptions
# except:
#    print ("Divided by zero")
#    print ("Done")

# except Exception as e:
#    print ("Error = ", e) # e gives teh message of teh exception
#    print (type(e))  # this will give the exact exception type that can be replaced in teh except block than generic Exception class
#    print ("Done")

except ZeroDivisionError as e:
    print ('Error = ', e)

except TypeError as e:
    print('Error = ', e)

# we can add Else and Finalle too to the try-except block

else: # else statement will not be executed whenever there is any exception
    print ('__else__')
finally: # it is gu')ranteed to execute, dosent matter error occurs or not
    print ('__finally__)


print("Result = ", result)
print('End')

print ("===================================== Raise and Exception ======================================================")
# functions would have raise Exception statements with some exception message
# code must have try-except block to handle the execution an dexception else the code will throw error

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



