# decorators wrap a function and modify its behaviour without changing the source code of the function
def decorator_func(func):
    def wrapper_func():
        print('X' * 20)
        func()
        print('x' * 10)
    return wrapper_func   # example of closure

'''
def say_hello():
    print('Hellow world')

hello = decorator_func(say_hello)
hello()
# this both line of declaing decorator can be replaced with onle line above teh function thas has to be decorated '@decorator_func'

'''
#hello = decorator_func(say_hello)
#hello()

@decorator_func
def say_hello():
    print('Hello world')

say_hello()

# multiple decorators can also be used with onefunction

print("==================================multiple decorators==================")


def decorator_x(func):
    def wrapper_func():
        print('X' * 20)
        func()
        print('x' * 10)
    return wrapper_func   # example of closure

def decorator_y(func):
    def wrapper_func():
        print('y' * 20)
        func()
        print('y' * 10)
    return wrapper_func   # example of closure

@decorator_y
@decorator_x
def say_hello():
    print('Hellow world')

# call th function
say_hello()

print( 'or the the notation of declaring decorators')

helloDec  = decorator_x(decorator_y(say_hello)) #comment the @decorator_y and @decorator_x before executing this line
helloDec()


print('=============another example==========')
def decorator_div(func):
    def wraper_func(x,y):
        if (y==0):
            print('division with 0 is not allowed')
            return 0
        return func(x,y)
    return wraper_func

@decorator_div
def divideFun(x,y):
    return x / y

print(divideFun(15,3))
print(divideFun(15,0))






