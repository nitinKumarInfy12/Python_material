# generator is a function that returns an iterator object we can iterate upon
# yeild is the keyword used in generators instead of return
 # with generator function, we dont need to implement the iterator class with iter(). next() functions
 # with generator function, we dont need to raise theStopIteration exception explicitly, generator funtion handles it internally

def myFunction():
    yield 'a'
    yield 'b'
    yield 'c'

myFun = myFunction()
'''
print(next(myFun))
print(next(myFun))
print(next(myFun))
'''
for i in myFun:
    print(i)

print('=================================')

# this will replace the whole ListIterator class we created in iterators
def ListIterator(list):
    for i in list:
        yield i

a = [3,2,5,6,8,7,9,10]
myList = ListIterator(a)

'''
print(next(myList))
print(next(myList))
print(next(myList))
print(next(myList))
print(next(myList))
print(next(myList))
print(next(myList))
print(next(myList))
print(next(myList))
print(next(myList))
''' #no need to explicitly implement the raise exception, its handled internally

for i in myList:
    print (i)









