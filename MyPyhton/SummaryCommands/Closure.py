#closure : returns function object without parenthesis
# closure function stores the value even if the outer function is deleted
# in closure, returns the inner function without the parenthesis
# nested functions; defining function within function
def nth_power (exponent):
    def pow_of(base):
        return pow(base, exponent)
    return pow_of

# return is returning a function.

square = nth_power(2)
print(square(2))
print(square(3))
print(square(4))

cube = nth_power(3)

print(cube(2))

del nth_power
print(square())

# closures can be used in place of class, when there is 1 method to definw within class
# closures can be used with decorators