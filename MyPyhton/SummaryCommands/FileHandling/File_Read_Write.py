# open : to open/write a fie in various modes
# write : to write contents in the file

#fh = open('demo.txt', 'w') # Overwrites the file
fh = open('demo.txt','a') # appends in th existing file


# fh.write('use open function to open the file, it takes 2 arguments, file name and the mode.')

try:
    for i in range(10):
        fh.write('this is the line number %d \n' % i)

finally:
    fh.close()


# following is the shorter and equivalent code for the above lines

# the with block will open and close the file, no need to explicity mention the command to close the file
# with open('C:\\Users\\nkum17\\Desktop\\17Sept_DesktopFiles\\SelfStudy\\Python_Study\\demo.txt', 'a') as fh:
with open('demo.txt', 'a') as fh:
    for i in range(10):
        fh.write('This is line number %d from the with statement\n' % i)