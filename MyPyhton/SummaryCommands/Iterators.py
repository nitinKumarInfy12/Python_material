# __iter__() and __next__()
'''
a = [2,5,3,6,8]

#print (dir (a)) gives teh list of functions/methods applicable to a

it = iter(a) # it returns the iterator for the object a

print(next(it)) # next gives teh element from iteratable objects
print(next(it)) # the next item of teh object
print(next(it)) # the next item of teh object


'''

# Create an iterator class

class ListIterator:
    def __init__(self, list):
        self.__list = list
        self.__index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.__index += 1
        if self.__index == len(self.__list):
            raise StopIteration
        return self.__list[self.__index]

a = [3,2,5,6,8,7,9,10]
it = ListIterator(a)
myList = iter(it)

# print(next(myList))
# print(next(myList))
# print(next(myList))
# print(next(myList))
# print(next(myList))
# print(next(myList))
# print(next(myList))

for i in myList:
    print (i)
