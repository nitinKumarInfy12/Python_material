from functools import reduce
# this is required or teh reduce function


def double(a):
    return a * 2

# lambda function of teh funtion: , anonymous functions without name,
# Lambda function is one line function

double = lambda x : x * 2


def add(x,y):
    return x + y

# lambda represent
add = lambda x,y : x + y

def product(x,y,z):
    return x * y * z

# lambda represent
product = lambda x,y,z : x * y * z

print(double(5))
print(add(10,14))
print(product(2,3,6))

# lambda function we use generally when it takes function as an argument and returns functs

print("==========================filter, reduce, map========================================")
# map function

list1= [2,4,5,8,7,6,3]
list2 = [5,3,8,9,4,1,6,7]

a = map(lambda x: x *2 , list1)
# print(a) need to cast the map output to list type
print(list(a))

b = map(lambda x,y :x + y, list1, list2)
print(list(b))

# filter function : function as argument should return boolean value only

c = filter(lambda x : x%2==0, list1)
print(list(c))

d = filter(lambda x: True if x > 4 else False, list1)
print('d = ', list(d))

# reduce function, need to import module functools,
# from functools import reduce
e = reduce(lambda x, y : x+y, list1)  # it will add first 2 elements into 1 and then so on an will return total sum of elements

print(e)




