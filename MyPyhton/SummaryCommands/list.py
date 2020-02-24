x = [3,5,6,8,6,10]
y = [2,4,'max', [3,5,4,7]]

print (x)
print (x[0])
print (x[3])
print (x[1:3])

print (y)

print (len(y))

# deletes the list
#del x

# clears the list elements
y.clear()
print (y)
y.insert(0,'Tom')
print (y)
a = x.count(6)

print (len(x))

column_names = [desc[0] for desc in cursor.description] # advanceway of creatign list 
'''
insert
pop
del
clear
sort
append
copy
count

'''