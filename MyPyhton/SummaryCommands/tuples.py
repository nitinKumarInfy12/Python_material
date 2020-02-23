# Tuples are immutable
#x= (1,3,5,7,8,10,7,'test')
x= (1,3,5,7,8,10,7)
print (x)


a= ('hi',)*5
print (a)
print (len(x))

print (x.index(5))

print (x.count(7))
print (len(x))
y = max(x)
print (y)
del a
print (a)


