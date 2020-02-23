#Plaintext files notepad or .py files
# binar files: PDF, word, excel, exe etc that cannot be read be  notepad
# shelve module to work with binary files
# bsic format
fh = open('demo.txt','a')

try:
    for i in range(10):
        fh.write("this is line no %d\n" %(i+1))

finally:
    fh.close()

# this whole line of codes above can be replaced with new format
# the following format performs all, TRy, finally, close

with open('demo.txt','a') as fh:
    for i in range(10):
        fh.write("this is line no %d\n" %(i+1))

# if file location has to be given, in windows \\ are requuired in place of \
with open('C:\\files\\demo.txt','a') as fh:
    for i in range(10):
        fh.write("this is line no %d\n" %(i+1))


# reading files in python
fh = open('demo.txt')
print(fh.read())
print(fh.read(4)) # reads 4 characters from te first line
print(fh.readline()) # reads the first line
print(fh.readline()) # reads the second line
#  readline starts from the pointer

print(fh.readlines()) # reads all line in form of list
#since it retruns list , we cna apply list function on it
print(fh.readlines()[4]) # returns the 5th line , 5th index item

# for loop can be used to iteate over teh lines
for line in fh:
    print (line) # prints line
    print (len(line)) # prints number of charactes in each line
    print(line.split(' ')) # splits the line in words using space
fh.close()


with open('demo.txt', 'r') as fh:
    for line in fh:
        print(line)


