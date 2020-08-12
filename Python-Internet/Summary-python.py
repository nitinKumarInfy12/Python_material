def ListIterator(list):
    for i in list:
        yield i

a = [3,2,5,6,8,7,9,10]
print(f'reverse list {a[::2]}')
myList = ListIterator(a)

print(next(myList))
print(next(myList))
print(next(myList))
print(next(myList))
print(next(myList))

print("@@@@@@@@@@@@@@@@@@@@@@")

for i in myList:
    print (i)