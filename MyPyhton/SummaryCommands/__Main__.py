# if __name__ == "__main__"     : the file which has this statement over any commnad, that command will get executed only if that file is executed as main file.

# create the following command in a seperate file, lets name teh file as mathpy.py
def add(a,b):
    return a + b

print (add(10,15))



# create another file, lets name it testpy.py
improt mathpy
print(mathpy.add(8,4))

#out puts will be
# 12
#25

# 25 was not expected to be printed , so to avoid that add if __name__ =+ "__main__" in the mathpy.py file over the print command
if __name__ == "__main__":
    print(add(10, 15))