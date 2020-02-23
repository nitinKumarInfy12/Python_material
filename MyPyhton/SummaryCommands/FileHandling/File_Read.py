fh = open('demo.txt', 'r') # r is teh default mode.

# read() is used to read the file

#print(fh.read())
#print(fh.read(4)) # reads the first 4 characters from the file, and sets the pointer to the nd of 4 characters
#print(fh.readline()) # reads the first line of the file from teh pointer location
#print(fh.readline())
#print(fh.readlines()) # reads all the lines and returns a list of lines

for line in fh:
    print(line) # retruns each line
    print(len(line)) # counts teh number ofcharacters in each line
    print(line.split(' ')) # splits the line with space delimiter
    print(len(line.split(' '))) #  counts the number of words in the line

fh.close()